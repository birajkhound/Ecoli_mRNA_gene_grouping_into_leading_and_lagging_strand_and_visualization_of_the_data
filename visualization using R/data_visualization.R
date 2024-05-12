library(readxl)
Leading_and_lagging_strend_of_ecoli <- read_excel("result2.xlsx")
View(Leading_and_lagging_strend_of_ecoli)

png(file='boxplot1.png')
boxplot(Start_GP~End_GP,data=Leading_and_lagging_strend_of_ecoli,xlab="Starting_Position_of_gene",ylab="Ending_Position_of_gene",main="Genes_of_Ecoli")
dev.off()

LES <- nrow(Leading_and_lagging_strend_of_ecoli[Leading_and_lagging_strend_of_ecoli$LES_LAS == "LeS", ])
LAS <- nrow(Leading_and_lagging_strend_of_ecoli[Leading_and_lagging_strend_of_ecoli$LES_LAS == "LaS", ])
x=c("les","las")
y=c(LES, LAS)
png(file="barchart_les_las.jpg")
barplot(y,names.arg=x,col="blue",border="red" ,xlab="Leading And Lagging strand",
        ylab="No of genes", main="Econi gene variation")
dev.off()

x=c(LES, LAS)
labels=c("les", "las")
piepercent=round(100*x/sum(x),1)
png(file="les_las_of_ecoli_mrna_colors_percentage_legend.jpg")
pie(x, labels=piepercent,main="Pie Chart of les_las_of_ecoli_mrna",col=rainbow(length(x)))
legend("topright", c("leading_strand", "lagging_strand"),cex=0.8,fill=rainbow(length(x)))
dev.off()


