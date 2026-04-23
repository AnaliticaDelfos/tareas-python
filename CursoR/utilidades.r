library(httr)
library(tidyverse)

guardar_11 <- function(df) {
    datos <- read_csv("cohorte_estudio.csv")
    cabeza <- datos |> head()
    son_iguales <- all.equal(cabeza, df)
    calificacion <- 0
    if (son_iguales) {
        calificacion <- 1
    }
    response <- POST(
        url = "https://calificar-r-435015279585.us-central1.run.app",
        body = list(JPY_SESSION_NAME = Sys.getenv("JPY_SESSION_NAME"), usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Guardado")
    content(response, "parsed")
}
