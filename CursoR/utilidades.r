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
    } else {
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
    } else {
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
    pacientes_criticos <- datos |>
        filter(glucosa_mgdl > 140) |>
        select(nombre, glucosa_mgdl)
    son_iguales <- all.equal(pacientes_criticos, df)
    calificacion <- 0
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    } else {
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
        select(nombre, glucosa_mgdl) |>
        arrange(desc(glucosa_mgdl))
    son_iguales <- all.equal(pacientes_hospitalizados, df)
    calificacion <- 0
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    } else {
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

guardar_15 <- function(df) {
    datos <- read_csv("cohorte_estudio.csv")
    pacientes_de_interes <- datos |>
        select(nombre, edad, glucosa_mgdl) |>
        filter(glucosa_mgdl > 126) |>
        arrange(desc(glucosa_mgdl))
    son_iguales <- all.equal(pacientes_de_interes, df)
    calificacion <- 0
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    } else {
        print("Vuélvelo a intentar :)")
    }
    response <- POST(
        url = "https://calificar-r-435015279585.us-central1.run.app",
        body = list(JPY_SESSION_NAME = "Notebook15", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}

guardar_16 <- function(df) {
    datos <- read_csv("cohorte_estudio.csv")
    df_resultado <- datos |>
        mutate(
            glucosa_ajustada = glucosa_mgdl + 10
        ) |>
        select(nombre, glucosa_ajustada)
    son_iguales <- all.equal(df_resultado, df)
    calificacion <- 0
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    } else {
        print("Vuélvelo a intentar :)")
    }
    response <- POST(
        url = "https://calificar-r-435015279585.us-central1.run.app",
        body = list(JPY_SESSION_NAME = "Notebook15", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}

guardar_17 <- function(df) {
    df_resultado <- datos |>
        mutate(
            prioridad = if_else(hospitalizado == TRUE, "Alta", "Baja")
        ) |>
        select(nombre, hospitalizado, prioridad)
    son_iguales <- all.equal(df_resultado, df)
    calificacion <- 0
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    } else {
        print("Vuélvelo a intentar :)")
    }
    response <- POST(
        url = "https://calificar-r-435015279585.us-central1.run.app",
        body = list(JPY_SESSION_NAME = "Notebook15", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}

guardar_18 <- function(df) {
    df_resultado <- datos |>
        group_by(sexo) |>
        summarise(total = n())
    son_iguales <- all.equal(df_resultado, df)
    calificacion <- 0
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    } else {
        print("Vuélvelo a intentar :)")
    }
    response <- POST(
        url = "https://calificar-r-435015279585.us-central1.run.app",
        body = list(JPY_SESSION_NAME = "Notebook15", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}


guardar_19 <- function(df) {
    df_resultado <- datos |>
        group_by(hospitalizado) |>
        summarise(
            promedio_edad = mean(edad),
            glucosa_maxima = max(glucosa_mgdl)
        )
    son_iguales <- all.equal(df_resultado, df)
    calificacion <- 0
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    } else {
        print("Vuélvelo a intentar :)")
    }
    response <- POST(
        url = "https://calificar-r-435015279585.us-central1.run.app",
        body = list(JPY_SESSION_NAME = "Notebook15", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}


guardar_20 <- function(df) {
    df_resultado <- datos |>
        mutate(condicion_glucosa = if_else(glucosa_mgdl >= 126, "Alta", "Normal")) |>
        group_by(hospitalizado) |>
        summarise(
            total = n(),
            promedio_edad = mean(edad),
            glucosa_maxima = max(glucosa_mgdl)
        )
    son_iguales <- all.equal(df_resultado, df)
    calificacion <- 0
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    } else {
        print("Vuélvelo a intentar :)")
    }
    response <- POST(
        url = "https://calificar-r-435015279585.us-central1.run.app",
        body = list(JPY_SESSION_NAME = "Notebook15", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}

guardar_21 <- function(variable) {
    resultado <- c("sexo", "glucosa_mgdl", "edad", "diagnostico")
    son_iguales <- variable %in% resultado
    calificacion <- 0
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    } else {
        print("Vuélvelo a intentar :)")
    }
    response <- POST(
        url = "https://calificar-r-435015279585.us-central1.run.app",
        body = list(JPY_SESSION_NAME = "Notebook15", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}

guardar_22 <- function(df) {
    datos <- read_csv("cohorte_limpieza.csv")
    mediana_peso <- median(datos$peso_kg, na.rm = TRUE)
    datos_limpios <- datos |> mutate(peso_kg = replace_na(peso_kg, mediana_peso))
    son_iguales <- all.equal(datos_limpios, df)
    calificacion <- 0
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    } else {
        print("Vuélvelo a intentar :)")
    }
    response <- POST(
        url = "https://calificar-r-435015279585.us-central1.run.app",
        body = list(JPY_SESSION_NAME = "Notebook15", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}

guardar_23 <- function(df) {
    datos <- read_csv("cohorte_limpieza.csv")
    pendiente_de_revision <- datos |>
        mutate(diagnostico = replace_na(diagnostico, "Pendiente de revisión"))
    df_resultado <- pendiente_de_revision |> count(diagnostico, sort = TRUE)
    son_iguales <- all.equal(df_resultado, df)
    calificacion <- 0
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    } else {
        print("Vuélvelo a intentar :)")
    }
    response <- POST(
        url = "https://calificar-r-435015279585.us-central1.run.app",
        body = list(JPY_SESSION_NAME = "Notebook15", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}


guardar_24 <- function(df) {
    datos <- read_csv("cohorte_limpieza.csv")
    df_resultado <- datos |>
        drop_na(glucosa_mgdl) |>
        filter(edad > 18)
    son_iguales <- all.equal(df_resultado, df)
    calificacion <- 0
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    } else {
        print("Vuélvelo a intentar :)")
    }
    response <- POST(
        url = "https://calificar-r-435015279585.us-central1.run.app",
        body = list(JPY_SESSION_NAME = "Notebook15", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}

guardar_25 <- function(df) {
    datos <- read_csv("cohorte_limpieza.csv")

    mediana_edad <- median(datos$edad, na.rm = TRUE)
    promedio_glucosa <- mean(datos$glucosa_mgdl, na.rm = TRUE)

    df_resultado <- datos |>
        mutate(
            edad = replace_na(edad, mediana_edad), glucosa_mgdl = replace_na(glucosa_mgdl, promedio_glucosa), sexo = replace_na(sexo, "U"),
            diagnostico = replace_na(diagnostico, "Sin registro")
        ) |>
        drop_na(peso_kg)
    son_iguales <- all.equal(df_resultado, df)
    calificacion <- 0
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    } else {
        print("Vuélvelo a intentar :)")
    }
    response <- POST(
        url = "https://calificar-r-435015279585.us-central1.run.app",
        body = list(JPY_SESSION_NAME = "Notebook15", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}

guardar_26 <- function() {
    
    son_iguales <- TRUE
    calificacion <- 0
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    } else {
        print("Vuélvelo a intentar :)")
    }
    response <- POST(
        url = "https://calificar-r-435015279585.us-central1.run.app",
        body = list(JPY_SESSION_NAME = "Notebook15", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}

guardar_27 <- function() {
    
    son_iguales <- TRUE
    calificacion <- 0
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    } else {
        print("Vuélvelo a intentar :)")
    }
    response <- POST(
        url = "https://calificar-r-435015279585.us-central1.run.app",
        body = list(JPY_SESSION_NAME = "Notebook15", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}

guardar_28 <- function() {
    
    son_iguales <- TRUE
    calificacion <- 0
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    } else {
        print("Vuélvelo a intentar :)")
    }
    response <- POST(
        url = "https://calificar-r-435015279585.us-central1.run.app",
        body = list(JPY_SESSION_NAME = "Notebook15", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}

guardar_29 <- function() {
    
    son_iguales <- TRUE
    calificacion <- 0
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    } else {
        print("Vuélvelo a intentar :)")
    }
    response <- POST(
        url = "https://calificar-r-435015279585.us-central1.run.app",
        body = list(JPY_SESSION_NAME = "Notebook15", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}

guardar_30 <- function() {
    
    son_iguales <- TRUE
    calificacion <- 0
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    } else {
        print("Vuélvelo a intentar :)")
    }
    response <- POST(
        url = "https://calificar-r-435015279585.us-central1.run.app",
        body = list(JPY_SESSION_NAME = "Notebook15", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}

guardar_31 <- function() {
    
    son_iguales <- TRUE
    calificacion <- 0
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    } else {
        print("Vuélvelo a intentar :)")
    }
    response <- POST(
        url = "https://calificar-r-435015279585.us-central1.run.app",
        body = list(JPY_SESSION_NAME = "Notebook15", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}

guardar_32 <- function() {
    
    son_iguales <- TRUE
    calificacion <- 0
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    } else {
        print("Vuélvelo a intentar :)")
    }
    response <- POST(
        url = "https://calificar-r-435015279585.us-central1.run.app",
        body = list(JPY_SESSION_NAME = "Notebook15", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}

guardar_33 <- function() {
    
    son_iguales <- TRUE
    calificacion <- 0
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    } else {
        print("Vuélvelo a intentar :)")
    }
    response <- POST(
        url = "https://calificar-r-435015279585.us-central1.run.app",
        body = list(JPY_SESSION_NAME = "Notebook15", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}

guardar_34 <- function() {
    
    son_iguales <- TRUE
    calificacion <- 0
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    } else {
        print("Vuélvelo a intentar :)")
    }
    response <- POST(
        url = "https://calificar-r-435015279585.us-central1.run.app",
        body = list(JPY_SESSION_NAME = "Notebook15", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}

guardar_35 <- function() {
    
    son_iguales <- TRUE
    calificacion <- 0
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    } else {
        print("Vuélvelo a intentar :)")
    }
    response <- POST(
        url = "https://calificar-r-435015279585.us-central1.run.app",
        body = list(JPY_SESSION_NAME = "Notebook15", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}