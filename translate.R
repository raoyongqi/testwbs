chunk_size = 1000

library(magrittr)
google_get_supported_languages <- function() {
  
  url <- "https://cloud.google.com/translate/docs/languages"
  
  if (!RCurl::url.exists(url)) {
    
    stop("The URL is not available.")
    
  }
  
  
  webpage <- rvest::read_html(url)
  
  table <- webpage %>% rvest::html_nodes('table')
  df <- table %>% rvest::html_table()
  df_lang <- df[[1]] %>% tibble::as_tibble()
  return(df_lang)
  
}

google_is_valid_language_code <- function(language_code) {
  
  
  if (language_code == "auto") {
    return(TRUE)
  }
  
  if (language_code %in% c(google_get_supported_languages()$`ISO-639 code`,"zh-CN","zh-TW")) {
    return(TRUE)
  } else {
    return(FALSE)
  }
}

google_translate_long_text <- function(text, target_language = "zh-CN", source_language = "auto", chunk_size = 1000) {
  if (!google_is_valid_language_code(target_language)) {
    stop("Invalid target language code.")
  }
  if (!google_is_valid_language_code(source_language)) {
    stop("Invalid source language code.")
  }
  
  # Function to split text into chunks
  split_text <- function(text, chunk_size) {
    split_indices <- seq(1, nchar(text), by = chunk_size)
    sapply(split_indices, function(i) substr(text, i, i + chunk_size - 1))
  }
  
  # Split text into chunks if it's too long
  if (nchar(text) > chunk_size) {
    text_chunks <- split_text(text, chunk_size)
  } else {
    text_chunks <- list(text)
  }
  
  # Translate each chunk
  translations <- sapply(text_chunks, function(chunk) {
    formatted_text <- urltools::url_encode(chunk)
    formatted_link <- paste0(
      "https://translate.google.com/m?tl=",
      target_language, "&sl=", source_language,
      "&q=", formatted_text
    )
    
    response <- httr::GET(formatted_link)
    translation <- httr::content(response) %>%
      rvest::html_nodes("div.result-container") %>%
      rvest::html_text()
    
    translation <- urltools::url_decode(translation)
    gsub("\n", "", translation)
  })
  
  # Combine translated chunks
  paste(translations, collapse = " ")
}

