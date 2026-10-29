require_relative "lib/crawlora/wattpad/version"

Gem::Specification.new do |spec|
  spec.name = "crawlora-wattpad"
  spec.version = Crawlora::Wattpad::VERSION
  spec.summary = "Wattpad API client for Crawlora (11 endpoints)"
  spec.description = "Ruby client for Crawlora's hosted Wattpad API. Covers story, author, search, category, language, and public comment data across 11 endpoints."
  spec.authors = ["Crawlora"]
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"
  spec.files = Dir["lib/**/*.rb", "README.md", "CHANGELOG.md", "LICENSE"]
  spec.require_paths = ["lib"]
  spec.homepage = "https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=wattpad-ruby-homepage"
  spec.metadata = { "source_code_uri" => "https://github.com/Crawlora-org/crawlora-wattpad", "documentation_uri" => "https://github.com/Crawlora-org/crawlora-wattpad/blob/main/ruby/README.md", "rubygems_mfa_required" => "true" }

end
