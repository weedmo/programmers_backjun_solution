def solution(bin1, bin2):
    bin_ = '0b'
    result = int(bin_+bin1,2) + int(bin_+bin2,2)
    return bin(result)[2:]