original_data <- read.csv("DnD_spells.csv")

original_data <- original_data[order(original_data$Name), ]

new_data <- data.frame(matrix(nrow = 0,
			      ncol = ncol(original_data)))

new_data <- setNames(new_data, colnames(original_data))

for (row in seq_len(nrow(original_data))) {

  if (original_data[row, "Name"] %in% new_data[, "Name"]) {
    new_data[nrow(new_data), "Class"] <-
	    paste0(new_data[nrow(new_data), "Class"], ", ", original_data[row, "Class"])
  } else {
    new_data <- rbind(new_data, original_data[row, ])
  }

}


write.csv(new_data, "spells_without_duplicates.csv", row.names = FALSE)
