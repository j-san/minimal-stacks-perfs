# Stage 1: Build
FROM rust:1.88-alpine AS builder

WORKDIR /app

RUN apk add --no-cache musl-dev

# Cache dependencies first
# COPY Cargo.toml Cargo.lock ./
COPY Cargo.toml ./
COPY src ./src
RUN cargo fetch

# Copy source and build
COPY . ./
RUN cargo build --release

# Stage 2: Run
FROM alpine

WORKDIR /app

COPY --from=builder /app/target/release/minimal-rust-app /app/server

EXPOSE 3000

CMD ["/app/server"]
