class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        '''
        m = 1
        n = 4 * (1+2)

        m = 2
        n = 4 * (3+2+3+4)

        m = 3
        n = 4 * (5+4+3+4+5+6) 

        m = m
        n = 4 * (m + 2(m+1) + 2(m+2) + 2(m+3) + ... + 2(m+m-1) + m+m)
          = 4 * [(m + 2*m + 2*m + 2*m + ... (m times)) +  2 * (1+2+3+...+(m-1))]
          = 4 * [m + 2*m*m + 2 * m*(m-1)/2]
          = 4 * [m + 2*m*m + m*m - m]
          = 4 * [3*m*m]
          = 12*m*m


        N(m) = n(1) + n(2) + n(3) + ... + n(m)
             = 12*1 + 12*4 + 12*9 + ... + 12*m*m
             = 12 * (1 + 4 + 9 + ... + m*m)
             = 12 * (m)*(m+1)*(2*m+1)/6
             = 2 * m*(m+1)*(2*m+1)
        '''
        
        n = m = 0
        while n < neededApples:
            m += 1
            n += 12*m*m
        return 8*m