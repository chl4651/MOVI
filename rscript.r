# rscript.r(Cumulative Bar Plot-Block type)
# Output Option('-o')
fun_output <- function(){
	flag = FALSE
	args <- commandArgs(trailingOnly = TRUE)

	# Graph Size Option('-s')
	x_length = 7
	y_length = 7
	if(length(args) != 0){
		for(i in 1:length(args)){
			if(args[i] == '-s'){
				x_length = as.double(args[i+1])
				y_length = as.double(args[i+2])
			}
		}
	}		
		
	if(length(args) != 0){
        	for(i in 1:length(args)){
                	if(args[i] == '-o'){
                        	flag = TRUE
				dir = paste("save", args[i+1], sep="/")
                        	if(args[i+2] == 'pdf')
                                	pdf(dir, width = x_length, height = y_length) # default width = 7, height = 7)
                        	#if(args[i+2] == 'wmf')
                                #	win.metafile(dir, width = x_length, height = y_length)
				# res(resolution-Pixel per Inch) required for converting pixel to inch.
                        	if(args[i+2] == 'png')
                                	png(dir, width = x_length, height = y_length, units = "in", res = 200)
                        	if(args[i+2] == 'jpg')
                                	jpeg(dir, width = x_length, height = y_length, units = "in", res = 200)
                        	if(args[i+2] == 'bmp')
                                	bmp(dir, width = x_length, height = y_length, units = "in", res = 200)
                        	if(args[i+2] == 'ps')
                                	postscript(dir, width = x_length, height = y_length)
                	}
        	}
	}		
	if(flag == FALSE){
        	pdf('save/B-Rplots.pdf', width = x_length, height = y_length, family = "mono")
	}
}
fun_output2 <- function(){
        # Graph Size Option('-s')
	args <- commandArgs(trailingOnly = TRUE)
        x_length = 7
        y_length = 7
        if(length(args) != 0){
                for(i in 1:length(args)){
                        if(args[i] == '-s'){
                                x_length = as.double(args[i+1])
                                y_length = as.double(args[i+2])
                        }
		}
        }
	jpeg('save/B-Rplot%03d.jpg', width = x_length, height = y_length, units="in", res=200)
}

fun_rwbs1 <- function(){ # block to rwbs, I/O Count
	most <- read.table("block_rwbs1.dat")
	most_matrix <- data.matrix(most)
	trans <- t(most_matrix)
	trans_select <- trans[, !colSums(trans)==0]
	yrange<-c(0,max(colSums(trans_select))*1.25)
	barplot(trans_select,  xlab = "rwbs type", ylab = "I/O Count", col=c("lightblue","lightgreen", "lightyellow"), ylim = yrange)
	legend("topleft", legend=c("Data", "Journal", "Meta"), pch=21, pt.bg=c("lightblue","lightgreen", "lightyellow"))
}
fun_rwbs2 <- function(){ # block to rwbs, I/O Count(%)
        most <- read.table("block_rwbs2.dat")
        most_matrix <- data.matrix(most)
        trans <- t(most_matrix)
        trans_select <- trans[, !colSums(trans)==0]
        yrange<-c(0,max(colSums(trans_select))*1.25)
        barplot(trans_select,  xlab = "rwbs type", ylab = "I/O Count(%)", col=c("lightblue","lightgreen", "lightyellow"), ylim = yrange)
        legend("topleft", legend=c("Data", "Journal", "Meta"), pch=21, pt.bg=c("lightblue","lightgreen", "lightyellow"))
}
fun_rwbs3 <- function(){ # block to rwbs, I/O Size(1024KB)
        most <- read.table("block_rwbs3.dat")
        most_matrix <- data.matrix(most)
        trans <- t(most_matrix)
        trans_select <- trans[, !colSums(trans)==0]
        yrange <- c(0,max(colSums(trans_select))*1.25)
        barplot(trans_select,  xlab = "rwbs type", ylab = "I/O Size(1024KB)", col=c("lightblue","lightgreen", "lightyellow"), ylim = yrange)
        legend("topleft", legend=c("Data", "Journal", "Meta"), pch=21, pt.bg=c("lightblue","lightgreen", "lightyellow"))
}
fun_rwbs4 <- function(){ # block to rwbs, I/O Size(%)
        most <- read.table("block_rwbs4.dat")
        most_matrix <- data.matrix(most)
        trans <- t(most_matrix)
        trans_select <- trans[, !colSums(trans)==0]
        yrange<-c(0,max(colSums(trans_select))*1.25)
        barplot(trans_select,  xlab = "rwbs type", ylab = "I/O Size(%)", col=c("lightblue","lightgreen", "lightyellow"), ylim = yrange)
        legend("topleft", legend=c("Data", "Journal", "Meta"), pch=21, pt.bg=c("lightblue","lightgreen", "lightyellow"))
}

fun_action <- function(){
        most <- read.table("block_action.dat")
        most_matrix <- data.matrix(most)
        trans <- t(most_matrix)
        trans_select <- trans[, !colSums(trans)==0]
        barplot(trans_select,  xlab = "action", ylab = "I/O Count", col=c("lightblue","lightgreen", "lightyellow"))
        legend("topleft", legend=c("Data", "Journal", "Meta"), pch=21, pt.bg=c("lightblue","lightgreen", "lightyellow"))
}
# Y-axis Option(-y)
fun_y <- function(){
        args <- commandArgs(trailingOnly = TRUE)
        flag = FALSE
        if(length(args) != 0){
                for(i in 1:length(args)){
                        if(args[i] == '-y'){
                                flag = TRUE
                                if(args[i+1] == 'c'){ # I/O Count
                                        fun_rwbs1()
					fun_rwbs2()
                                }
                                if(args[i+1] == 's'){ # I/O Size
                                	fun_rwbs3()
					fun_rwbs4()
                                }
                                if(args[i+1] == 'all'){
                                	fun_rwbs1()
					fun_rwbs2()
					fun_rwbs3()
					fun_rwbs4()
                                }
                        }
                }
        }
        if(flag == FALSE){ # all is default
                fun_rwbs1()
		fun_rwbs2()
		fun_rwbs3()
		fun_rwbs4()
        }
}

# main
main <- function(){
	fun_output()
	fun_y()
	fun_output2()
	fun_y()
	garbage <- dev.off()
}
main()

