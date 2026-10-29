use crawlora_wattpad::{Client, ModelWattpadSearchResponseDoc, WattpadSearchParams};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = std::env::var("CRAWLORA_API_KEY")?;
    let client = Client::new(api_key)?;
    let response = client
        .wattpad
        .search(WattpadSearchParams {
            query: Some("romance".to_owned()),
            ..Default::default()
        })
        .await?;
    let data: ModelWattpadSearchResponseDoc = response.into_json()?;
    println!("{data:#?}");
    Ok(())
}
