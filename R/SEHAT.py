import matplotlib.pyplot as plt
import numpy as np

# Data
villages = ['ATLA', 'AUTANWALI', 'BAJEWALI', 'BANAWALI', 'BEHMAN', 'BEHMAN JASSA', 'BEHNIWAL',
            'BEHNIWAL G.S.', 'BHAI DESA', 'BIREWALI', 'CHEHLANWALI', 'CHEHLANWALI G.S.',
            'DALIYEWALI', 'DHINGER', 'DHINGER G.S.', 'DOOMWALI', 'FATTE', 'G.S. CHEHLANWALI',
            'JAGA RAM TIRATH', 'JAGARAM', 'JAGARAM TIRATH', 'JHANKIYAN', 'JHERIANWALI', 'KAMALU',
            'KARAMGARH', 'KHURD', 'LEHRI', 'MAKHA', 'MANSA', 'MAUD', 'MAUR', 'MOOSA G.S.', 'MOUD',
            'NAGLA', 'PERON', 'RAIPUR', 'RAIPUR G.S.', 'RAMDITEWALA', 'SHERON', 'TALWANDI AKLIA',
            'TANDIAN']

males = [3, 133, 1, 346, 2, 1, 178, 21, 0, 0, 255, 41, 327, 344, 13, 0, 0, 54, 0, 2, 1, 0, 114, 421,
         1, 0, 0, 56, 8, 5, 2, 62, 0, 1, 421, 358, 49, 0, 0, 430, 2]
females = [0, 70, 0, 376, 3, 2, 235, 24, 1, 2, 411, 74, 382, 520, 22, 2, 0, 96, 1, 3, 1, 1, 104, 390,
           0, 1, 3, 82, 8, 2, 1, 66, 1, 0, 480, 275, 33, 1, 1, 505, 0]

# Plotting
x = np.arange(len(villages))
width = 0.3

fig, ax = plt.subplots(figsize=(20, 10))
ax.bar(x - width, males, width, label='Male', color='blue')
ax.bar(x, females, width, label='Female', color='pink')

# Labels and Titles
ax.set_xlabel('Villages')
ax.set_ylabel('Number of Participants')
ax.set_title('Health Camp Attendance by Village (SEHAT Project)')
ax.set_xticks(x)
ax.set_xticklabels(villages, rotation=90)
ax.legend()

plt.tight_layout()
plt.show()
