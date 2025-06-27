# Stage 1: Build
FROM golang:1.22-alpine AS builder

WORKDIR /app

# Copy go.mod and go.sum first for better caching
COPY go.mod ./
RUN go mod download

COPY . ./
RUN go build -o server .

# Stage 2: Run
FROM alpine

WORKDIR /app

COPY --from=builder /app/server .

EXPOSE 3000

ENTRYPOINT ["/app/server"]
