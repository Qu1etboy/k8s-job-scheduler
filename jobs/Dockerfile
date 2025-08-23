FROM golang:1.24.3-alpine AS builder
WORKDIR /app
COPY go.mod ./
RUN go mod download
COPY . .

# Build all binaries
RUN CGO_ENABLED=0 GOOS=linux go build -o sync-data-job ./cmd/sync_data_job
RUN CGO_ENABLED=0 GOOS=linux go build -o cleanup-data-job ./cmd/clean_up_data_job

FROM alpine:latest
RUN apk --no-cache add ca-certificates tzdata
WORKDIR /root/

COPY --from=builder /app/sync-data-job .
COPY --from=builder /app/cleanup-data-job .