# Stage 1: Build
FROM maven:3.9-eclipse-temurin-21-alpine AS build

WORKDIR /app

COPY pom.xml .
RUN mvn dependency:go-offline

COPY src ./src
RUN mvn clean package -DskipTests

# Stage 2: Run
FROM eclipse-temurin:21-jre-alpine

WORKDIR /app

COPY --from=build /app/target/java-app-1.0.0.jar app.jar

EXPOSE 3000

ENV PORT=3000

ENTRYPOINT ["java", "-jar", "/app/app.jar"]
