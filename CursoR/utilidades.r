library(httr)
library(tidyverse)

guardar_11 <- function(df) {
    datos <- read_csv("cohorte_estudio.csv")
    cabeza <- datos |> head()
    son_iguales <- all.equal(cabeza, df)
    calificacion <- 0
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    }else{
        print("Vuélvelo a intentar :)")
    }
    response <- POST(
        url = "https://calificar-r-435015279585.us-central1.run.app",
        body = list(JPY_SESSION_NAME = "Notebook11", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}

guardar_12 <- function(df) {
    datos <- read_csv("cohorte_estudio.csv")
    tabla_reducida <- datos |> select(nombre, edad, hospitalizado)
    son_iguales <- all.equal(tabla_reducida, df)
    calificacion <- 0
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    }else{
        print("Vuélvelo a intentar :)")
    }
    response <- POST(
        url = "https://calificar-r-435015279585.us-central1.run.app",
        body = list(JPY_SESSION_NAME = "Notebook12", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}

guardar_13 <- function(df) {
    datos <- read_csv("cohorte_estudio.csv")
    pacientes_criticos <- datos |> filter(glucosa_mgdl > 140) |> select(nombre, glucosa_mgdl)
    son_iguales <- all.equal(pacientes_criticos, df)
    calificacion <- 0
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    }else{
        print("Vuélvelo a intentar :)")
    }
    response <- POST(
        url = "https://calificar-r-435015279585.us-central1.run.app",
        body = list(JPY_SESSION_NAME = "Notebook13", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}

guardar_14 <- function(df) {
    datos <- read_csv("cohorte_estudio.csv")
    pacientes_hospitalizados <- datos |> 
        filter(hospitalizado == TRUE) |> 
        select(nombre, glucosa_mgdl)  |> 
        arrange(glucosa_mgdl)
    son_iguales <- all.equal(pacientes_hospitalizados, df)
    calificacion <- 0
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    }else{
        print("Vuélvelo a intentar :)")
    }
    response <- POST(
        url = "https://calificar-r-435015279585.us-central1.run.app",
        body = list(JPY_SESSION_NAME = "Notebook14", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}