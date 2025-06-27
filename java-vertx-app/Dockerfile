# Stage 1: Build
FROM maven:3.9-eclipse-temurin-21-alpine AS build

WORKDIR /app

COPY pom.xml .
RUN mvn dependency:go-offline

COPY src ./src
RUN mvn clean package -DskipTests

CMD ["java", "-jar", "/app/target/starter-1.0.0-SNAPSHOT-fat.jar"]

# Stage 2: Run
FROM eclipse-temurin:21-jre-alpine

WORKDIR /app

COPY --from=build /app/target/starter-1.0.0-SNAPSHOT-fat.jar app.jar

EXPOSE 3000

ENV PORT=3000

CMD ["java", "-jar", "/app/app.jar"]
