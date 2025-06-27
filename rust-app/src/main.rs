use axum::{
    routing::get,
    Router,
};
use std::net::SocketAddr;
// use hyper::server;

#[tokio::main]
async fn main() {
    // Create axum router
    let app = Router::new().route("/", get(|| async { "Hello, world!" }));

    // Get port from env or default
    let addr = "0.0.0.0:3000";
    let listen = tokio::net::TcpListener::bind(addr).await.unwrap();

    println!("Server running on http://{}", addr);
    axum::serve(listen, app).await.unwrap();
}

