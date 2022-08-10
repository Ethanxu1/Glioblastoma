args <- commandArgs(trailingOnly = TRUE)

#options(warn=-1)
Gender=as.integer(args[1])
Age=as.numeric(args[2])
EOR=as.integer(args[3])
Ki.67=as.integer(args[4])
Grade=as.integer(args[5])
Location=as.integer(args[6])
Tumor.Side=as.integer(args[7])
Diameter=as.numeric(args[8])
Chemotherapy=as.integer(args[9])
Radiotherapy=as.integer(args[10])
Polysomy_Status=as.integer(args[11])
fn=args[12]

dat=data.frame(Gender=Gender,
Age=Age,
EOR=EOR,
Ki.67=Ki.67,
Grade=Grade,
Location=Location,
Tumor.Side=Tumor.Side,
Diameter=Diameter,
Chemotherapy=Chemotherapy,
Radiotherapy=Radiotherapy,
Polysomy_Status=Polysomy_Status
)

dat$Location <- factor(dat$Location,levels=c(1,2,3))
dat$Tumor.Side <- factor(dat$Tumor.Side,levels=c(1,2,3))
dat$Polysomy_Status <- factor(dat$Polysomy_Status,levels=c(0,1,2))

library(randomForestSRC)
load("./Data/rfsrc.RData")

pred <- predict.rfsrc(rfsrc_df_yo, newdata = dat, na.action="na.impute")

jpeg(paste0("./tmp/",fn,"_surv.jpg"),height=500,width=700,quality=100)
plot(pred$time.interest,pred$survival,type="l",ylim=c(0,1),xlab="Time (Day)",
    ylab="Probability of Survival",cex.lab=1.5,lwd=3,cex.axis=1.5)
graphics.off()

pred <- predict.rfsrc(rfsrc_df_yp, newdata = dat, na.action="na.impute")

jpeg(paste0("./tmp/",fn,"_relapse.jpg"),height=500,width=700,quality=100)
plot(pred$time.interest,1-pred$survival,type="l",ylim=c(0,1),xlab="Time (Day)",
    ylab="Probability of Recurrence",cex.lab=1.5,lwd=3,cex.axis=1.5)
graphics.off()




