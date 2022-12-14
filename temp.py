import numpy as np

# define the number of nodes
n = 38

# define the dsm
dsm = np.identity(n)

dsm[0][2] = 1
dsm[0][3] = 1
dsm[0][7] = 1
dsm[0][10] = 1
dsm[0][32] = 1
dsm[0][35] = 1

dsm[1][7] = 1
dsm[1][8] = 1
dsm[1][32] = 1

dsm[2][10] = 1
dsm[2][13] = 1
dsm[2][14] = 1
dsm[2][29] = 1
dsm[2][35] = 1

dsm[3][7] = 1
dsm[3][13] = 1
dsm[3][29] = 1
dsm[3][35] = 1

dsm[4][5] = 1
dsm[4][6] = 1
dsm[4][20] = 1
dsm[4][25] = 1
dsm[4][36] = 1

dsm[5][6] = 1
dsm[5][20] = 1

dsm[6][20] = 1
dsm[6][22] = 1
dsm[6][23] = 1
dsm[6][37] = 1

dsm[7][8] = 1
dsm[7][14] = 1
dsm[7][22] = 1
dsm[7][23] = 1
dsm[7][28] = 1
dsm[7][29] = 1
dsm[7][30] = 1
dsm[7][31] = 1
dsm[7][32] = 1
dsm[7][33] = 1
dsm[7][34] = 1

dsm[8][28] = 1
dsm[8][29] = 1

dsm[9][12] = 1
dsm[9][13] = 1
dsm[9][18] = 1
dsm[9][33] = 1
dsm[9][34] = 1

dsm[10][13] = 1
dsm[10][17] = 1
dsm[10][35] = 1

dsm[11][19] = 1
dsm[11][27] = 1
dsm[11][36] = 1

dsm[12][13] = 1

dsm[13][14] = 1
dsm[13][16] = 1
dsm[13][17] = 1

dsm[14][16] = 1
dsm[14][18] = 1
dsm[14][26] = 1
dsm[14][27] = 1
dsm[14][29] = 1

dsm[15][31] = 1
dsm[15][32] = 1

dsm[16][17] = 1
dsm[16][26] = 1

dsm[17][35] = 1

dsm[18][19] = 1
dsm[18][24] = 1
dsm[18][27] = 1
dsm[18][28] = 1
dsm[18][29] = 1

dsm[19][24] = 1
dsm[19][27] = 1
dsm[19][36] = 1

dsm[20][24] = 1
dsm[20][25] = 1
dsm[20][27] = 1
dsm[20][36] = 1
dsm[20][37] = 1

dsm[21][31] = 1

dsm[22][23] = 1
dsm[22][27] = 1
dsm[22][28] = 1
dsm[22][29] = 1
dsm[22][37] = 1

dsm[23][31] = 1
dsm[23][37] = 1

dsm[24][25] = 1
dsm[24][27] = 1
dsm[24][28] = 1
dsm[24][29] = 1
dsm[24][37] = 1

dsm[25][27] = 1
dsm[25][36] = 1
dsm[25][37] = 1

dsm[26][27] = 1
dsm[26][29] = 1

dsm[27][28] = 1
dsm[27][29] = 1
dsm[27][37] = 1

dsm[28][29] = 1
dsm[28][37] = 1

dsm[29][33] = 1
dsm[29][34] = 1

dsm[30][31] = 1
dsm[30][32] = 1

dsm[31][32] = 1

# make dsm symmetric
for i in range(len(dsm)):
    for j in range(len(dsm[0])):
        if dsm[i][j] == 1:
            dsm[j][i] == 1

print(dsm)