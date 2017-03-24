bool RH_ASK::send(const uint8_t* data, uint8_t len)
{
    uint8_t i;
    uint16_t index = 0;
    uint16_t crc = 0xffff;
    uint8_t *p = _txBuf + RH_ASK_PREAMBLE_LEN; // start of the message area
    uint8_t count = len + 3 + RH_ASK_HEADER_LEN; // Added byte count and FCS and headers to get total number of bytes

    if (len > RH_ASK_MAX_MESSAGE_LEN)
	return false;

    // Wait for transmitter to become available
    waitPacketSent();

    // Encode the message length
    crc = RHcrc_ccitt_update(crc, count); 
    p[index++] = symbols[count >> 4]; //  p[0] = 00001000 >> 4 = 00000000 = symbol[0]
    p[index++] = symbols[count & 0xf]; // p[1] = 00000000 & 00001111 = 0000 = symbol[0]
										//	p[] = {0xd,0xd} index = 2 
    // Encode the headers
    crc = RHcrc_ccitt_update(crc, _txHeaderTo);
    p[index++] = symbols[_txHeaderTo >> 4]; // p[2] = 11111111 >> 4 = 00001111 = symbol[15]
    p[index++] = symbols[_txHeaderTo & 0xf];// p[3] = 00001111 & 00001111 = 1111 = symbol[15]
    crc = RHcrc_ccitt_update(crc, _txHeaderFrom);
    p[index++] = symbols[_txHeaderFrom >> 4]; // p[4]= 11111111 >> 4 = 00001111 = symbol[15] 
    p[index++] = symbols[_txHeaderFrom & 0xf]; // p[5] = 00001111 & 00001111 = 1111 = symbol[15]
    crc = RHcrc_ccitt_update(crc, _txHeaderId);
    p[index++] = symbols[_txHeaderId >> 4]; // p[6] = 00000000 >> 4 = 00000000 = symbol[0] 
    p[index++] = symbols[_txHeaderId & 0xf];// p[7] = 00000000 & 00001111 = 00000000 = symbol[0]
    crc = RHcrc_ccitt_update(crc, _txHeaderFlags);
    p[index++] = symbols[_txHeaderFlags >> 4]; // p[8] = 00000000 >> 4 = 00000000 = symbol[0] 
    p[index++] = symbols[_txHeaderFlags & 0xf]; //  p[9] = 00000000 & 00001111 = 00000000 = symbol[0]
												//index = 10
												// 	p[] = {0xd,0xd, 0x34, 0x34, 0x34, 0x34 0xd, 0xd, 0xd, 0xd }

    // Encode the message into 6 bit symbols. Each byte is converted into 
    // 2 6-bit symbols, high nybble first, low nybble second
    for (i = 0; i < len; i++)
    {
	crc = RHcrc_ccitt_update(crc, data[i]);			//data[] = {'H'}
	p[index++] = symbols[data[i] >> 4]; 		// p[10] = 01001000 >> 4 = 00000100 = symbol[4]
	p[index++] = symbols[data[i] & 0xf];		//p[11] = 00000100 & 00001111 = 0100 = symbol[4]
    }
												//p[] = {0xd,0xd, 0x34, 0x34, 0x34, 0x34 0xd, 0xd, 0xd, 0xd, 0x16, 0x16 }
												// index = 12
    // Append the fcs, 16 bits before encoding (4 6-bit symbols after encoding)
    // Caution: VW expects the _ones_complement_ of the CCITT CRC-16 as the FCS
    // VW sends FCS as low byte then hi byte
    crc = ~crc;
    p[index++] = symbols[(crc >> 4)  & 0xf];
    p[index++] = symbols[crc & 0xf];
    p[index++] = symbols[(crc >> 12) & 0xf];
    p[index++] = symbols[(crc >> 8)  & 0xf];

    // Total number of 6-bit symbols to send
    _txBufLen = index + RH_ASK_PREAMBLE_LEN; //_txBufLen = 16 + 8 = 24

    // Start the low level interrupt handler sending symbols
    setModeTx();

// FIXME
    thisASKDriver = this;

    return true;
}


uint16_t RHcrc_ccitt_update (uint16_t crc, uint8_t data)
{
    data ^= lo8 (crc); // data = data ^ (0xffff & 0xff) = data ^ 0xff 
    data ^= data << 4; // data= data ^(data << 4) 
    
    return ((((uint16_t)data << 8) | hi8 (crc)) ^ (uint8_t)(data >> 4) 
	    ^ ((uint16_t)data << 3));
}