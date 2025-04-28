rm(list=ls())
data <- read.csv("imaging1_hc_AP_CP.csv", header=TRUE)

# Define data for Group 0
data_group_0 <- subset(data, Condition == 0)

# Define data for Group 1
data_group_1 <- subset(data, Condition == 1) #comparing predictions with those of the healthy controls to assess differences

age=data$Age
sex=data$Sex
brainage=data_group_1$LR_T1_corrected
delta=brainage-age
data$delta <- brainage - age
group=data$Condition
model <- lm(delta ~ group + age + sex, data = data)
anova(model)
summary(model)


result <- aggregate(delta ~ group, data = data, FUN = function(x) c(mean = mean(x, na.rm = TRUE), sd = sd(x, na.rm = TRUE)))
print(result)

#Assess association between delta and biomedical/lifestyle/behavioral factors
smoking=data$smoking
alcohol=data$alcohol_intake
physical_activity=data$activity
neuroticism=data$neuroticism_score
sleep=data$sleep_score
creactiveprotein=data$crp
model <- lm(delta ~ neuroticism + age + sex, data = data)
summary(model)

model <- lm(delta ~ smoking + age + sex, data = data)
summary(model)

model <- lm(delta ~ alcohol + age + sex, data = data)
summary(model)

model <- lm(delta ~ physical_activity + age + sex, data = data)
summary(model)

model <- lm(delta ~ sleep + age + sex, data = data)
summary(model)

model <- lm(delta ~ creactiveprotein + age + sex, data = data)
summary(model)
