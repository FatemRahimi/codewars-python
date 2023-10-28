# Given BigInt variable extract length of bits starting from least significant bit* and skipping offset of bits. For convenience sake only first 64 bits of input variable will be used for encoding value. offset and length may be arbitrarily large.

# All input values will be non-negative.

# Examples

# input	offset	length	result
# 0xAF	4	0	0x0
# 0xAF	0	4	0xF
# 0xAF	4	4	0xA
# 0xAB00EF	4	16	0xB00E
# 0xAA00BB00CC	0xF0000000	0x64	0x0
# *LSb - Least Significant bit - bit denoting smallest value in the number i.e. 0 or 1.

function extractBits(field, offset, length) {
  if (offset >= 64 || length < 1 || field == 0n) return 0n;
  field >>= BigInt(offset);
  if (length >= 64) return field;
  let w = length >= 64 ? ~0n : (1n << BigInt(length)) - 1n;
  return field & w;
}


# 

function extractBits(field, offset, length) {
  const maxBits = 64n;
  const limit = length + offset & 2n * maxBits - 1n;
  const mask = 2n ** maxBits - 1n >> maxBits - limit;
  return (field & mask) >> offset;
}