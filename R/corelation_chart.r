# Load necessary libraries
install.packages("ggcorrplot")  # Install if needed
library(ggcorrplot)

# Sample correlation matrix (Replace with your actual data)
cor_matrix <- matrix(c(1, 0.483, 0.680, 0.753, 0.724,
                       0.483, 1, 0.456, 0.554, 0.418,
                       0.680, 0.456, 1, 0.673, 0.653,
                       0.753, 0.554, 0.673, 1, 0.739,
                       0.724, 0.418, 0.653, 0.739, 1), 
                     nrow = 5, byrow = TRUE)

# Variable names
colnames(cor_matrix) <- rownames(cor_matrix) <- c("Interpersonal Skills", "Attitude Toward Women Role", 
                                                  "Family Support", "Social Activity", "Decision Making")

# Create a heatmap
ggcorrplot(cor_matrix, method = "circle", type = "lower", lab = TRUE)
