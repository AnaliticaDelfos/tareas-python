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
        body = list(JPY_SESSION_NAME = "Notebook16", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
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
        body = list(JPY_SESSION_NAME = "Notebook17", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
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
        body = list(JPY_SESSION_NAME = "Notebook18", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
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
        body = list(JPY_SESSION_NAME = "Notebook19", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
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
        body = list(JPY_SESSION_NAME = "Notebook20", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
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
        body = list(JPY_SESSION_NAME = "Notebook21", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
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
        body = list(JPY_SESSION_NAME = "Notebook22", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
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
        body = list(JPY_SESSION_NAME = "Notebook23", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
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
        body = list(JPY_SESSION_NAME = "Notebook24", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
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
        body = list(JPY_SESSION_NAME = "Notebook25", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
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
        body = list(JPY_SESSION_NAME = "Notebook26", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
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
        body = list(JPY_SESSION_NAME = "Notebook27", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
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
        body = list(JPY_SESSION_NAME = "Notebook28", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
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
        body = list(JPY_SESSION_NAME = "Notebook28", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
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
        body = list(JPY_SESSION_NAME = "Notebook30", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
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
        body = list(JPY_SESSION_NAME = "Notebook31", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
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
        body = list(JPY_SESSION_NAME = "Notebook32", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
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
        body = list(JPY_SESSION_NAME = "Notebook33", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
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
        body = list(JPY_SESSION_NAME = "Notebook34", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
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
        body = list(JPY_SESSION_NAME = "Notebook35", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}

guardar_36 <- function(df) {
    r1_p_valor <- 0.1455
    r2_es_normal <- TRUE
    r3_camino <- "Parametrica"
    df_respuesta <- data.frame(
    pregunta = c("p_valor", "es_normal", "camino_sugerido"),
    respuesta = c(as.character(r1_p_valor), as.character(r2_es_normal), r3_camino)
    )
    son_iguales <- all.equal(df_respuesta, df)
    calificacion <- 0
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    } else {
        print("Vuélvelo a intentar :)")
    }
    response <- POST(
        url = "https://calificar-r-435015279585.us-central1.run.app",
        body = list(JPY_SESSION_NAME = "Notebook36", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}

guardar_37 <- function(df) {
    r1_p_valor <- 0.4386
    r2_significativo <- FALSE
    r3_incluye_cero <- TRUE
    df_respuesta <- data.frame(
        pregunta = c("p_valor", "significancia", "ic_cero"),
        respuesta = c(as.character(r1_p_valor), as.character(r2_significativo), as.character(r3_incluye_cero))
    )
    son_iguales <- all.equal(df_respuesta, df)
    calificacion <- 0
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    } else {
        print("Vuélvelo a intentar :)")
    }
    response <- POST(
        url = "https://calificar-r-435015279585.us-central1.run.app",
        body = list(JPY_SESSION_NAME = "Notebook37", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}

guardar_38 <- function(df) {
    r1_p_valor <- 0.8164
    r2_significativo <- FALSE
    r3_grupo_mayor <- "NO"
    df_respuesta <- data.frame(
        pregunta = c("p_valor", "significancia", "mediana_superior"),
        respuesta = c(as.character(r1_p_valor), as.character(r2_significativo), r3_grupo_mayor)
    )
    son_iguales <- all.equal(df_respuesta, df)
    calificacion <- 0
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    } else {
        print("Vuélvelo a intentar :)")
    }
    response <- POST(
        url = "https://calificar-r-435015279585.us-central1.run.app",
        body = list(JPY_SESSION_NAME = "Notebook38", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}

guardar_39 <- function(df) {
    r1_p_valor <- 0.1345
    r2_existe_asociacion <- FALSE
    r3_diagnostico_riesgo <- "Diabetes"
    df_respuesta <- data.frame(
        pregunta = c("p_valor", "asociacion", "riesgo_alto"),
        respuesta = c(as.character(r1_p_valor), r2_existe_asociacion, r3_diagnostico_riesgo)
    )
    son_iguales <- all.equal(df_respuesta, df)
    calificacion <- 0
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    } else {
        print("Vuélvelo a intentar :)")
    }
    response <- POST(
        url = "https://calificar-r-435015279585.us-central1.run.app",
        body = list(JPY_SESSION_NAME = "Notebook39", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}

guardar_40 <- function(df) {
    r1_normal_a <- TRUE
    r2_p_estatura <- 0.6731
    r3_sig_glucosa_b <- FALSE
    r4_asociacion_c <- FALSE
    df_respuesta <- data.frame(
        item = c("normalidad_a", "p_valor_a", "sig_wilcoxon_b", "asociacion_chi_c"),
        valor = c(as.character(r1_normal_a),
                    as.character(r2_p_estatura),
                    as.character(r3_sig_glucosa_b),
                    as.character(r4_asociacion_c))
    )
    son_iguales <- all.equal(df_respuesta, df)
    calificacion <- 0
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    } else {
        print("Vuélvelo a intentar :)")
    }
    response <- POST(
        url = "https://calificar-r-435015279585.us-central1.run.app",
        body = list(JPY_SESSION_NAME = "Notebook40", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}

guardar_41 <- function(df) {
    r1_rho <- -0.0069
    r2_p_valor <- 0.9222
    r3_es_significativa <- FALSE
    r4_direccion <- "Negativa"
    df_respuesta <- data.frame(
    pregunta = c("rho", "p_valor", "significancia", "direccion"),
    respuesta = c(as.character(r1_rho),
                    as.character(r2_p_valor),
                    as.character(r3_es_significativa),
                    as.character(r4_direccion))
    )
    son_iguales <- all.equal(df_respuesta, df)
    calificacion <- 0
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    } else {
        print("Vuélvelo a intentar :)")
    }
    response <- POST(
        url = "https://calificar-r-435015279585.us-central1.run.app",
        body = list(JPY_SESSION_NAME = "Notebook41", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}

guardar_42 <- function(df) {
    r1_intercepto <- 79.651
    r2_pendiente <- -2.911
    r3_es_significativo <- FALSE
    r4_logica_clinica <- FALSE
    df_respuesta <- data.frame(
    pregunta = c("intercepto", "pendiente", "significancia", "tendencia"),
    respuesta = c(as.character(r1_intercepto),
                    as.character(r2_pendiente),
                    as.character(r3_es_significativo),
                    as.character(r4_logica_clinica))
    )
    son_iguales <- all.equal(df_respuesta, df)
    calificacion <- 0
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    } else {
        print("Vuélvelo a intentar :)")
    }
    response <- POST(
        url = "https://calificar-r-435015279585.us-central1.run.app",
        body = list(JPY_SESSION_NAME = "Notebook42", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}

guardar_43 <- function() {
    
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
        body = list(JPY_SESSION_NAME = "Notebook43", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}

guardar_44 <- function(df) {
    r1_r2_ajustado <- -0.0023
    r2_es_robusto <- FALSE
    r3_mejoro_modelo <- FALSE
    df_respuesta <- data.frame(
        pregunta = c("r_cuadrado", "evaluacion_calidad", "mejora_por_edad"),
        respuesta = c(as.character(r1_r2_ajustado),
                        as.character(r2_es_robusto),
                        as.character(r3_mejoro_modelo))
    )
    son_iguales <- all.equal(df_respuesta, df)
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    } else {
        print("Vuélvelo a intentar :)")
    }
    response <- POST(
        url = "https://calificar-r-435015279585.us-central1.run.app",
        body = list(JPY_SESSION_NAME = "Notebook44", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}

guardar_45 <- function(df) {
    r1_calidad_modelo <- -0.0053
    r2_sexo_sig <- FALSE
    r3_coef_edad <- -0.0480
    r4_impacto_dominante <- "edad"
    df_respuesta <- data.frame(
        item = c("bondad_ajuste", "significancia_sexo", "efecto_edad", "lider_predictor"),
        valor = c(as.character(r1_calidad_modelo),
                as.character(r2_sexo_sig),
                as.character(r3_coef_edad),
                r4_impacto_dominante)
    )   
    son_iguales <- all.equal(df_respuesta, df)
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    } else {
        print("Vuélvelo a intentar :)")
    }
    response <- POST(
        url = "https://calificar-r-435015279585.us-central1.run.app",
        body = list(JPY_SESSION_NAME = "Notebook45", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}

#################################################################################

guardar_46 <- function(df) {
    r1_calidad_modelo <- -0.0053
    r2_sexo_sig <- FALSE
    r3_coef_edad <- -0.0480
    r4_impacto_dominante <- "edad"
    df_respuesta <- data.frame(
        item = c("bondad_ajuste", "significancia_sexo", "efecto_edad", "lider_predictor"),
        valor = c(as.character(r1_calidad_modelo),
                as.character(r2_sexo_sig),
                as.character(r3_coef_edad),
                r4_impacto_dominante)
    )   
    son_iguales <- all.equal(df_respuesta, df)
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    } else {
        print("Vuélvelo a intentar :)")
    }
    response <- POST(
        url = "https://calificar-r-435015279585.us-central1.run.app",
        body = list(JPY_SESSION_NAME = "Notebook46", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}

guardar_47 <- function(df) {
    r1_calidad_modelo <- -0.0053
    r2_sexo_sig <- FALSE
    r3_coef_edad <- -0.0480
    r4_impacto_dominante <- "edad"
    df_respuesta <- data.frame(
        item = c("bondad_ajuste", "significancia_sexo", "efecto_edad", "lider_predictor"),
        valor = c(as.character(r1_calidad_modelo),
                as.character(r2_sexo_sig),
                as.character(r3_coef_edad),
                r4_impacto_dominante)
    )   
    son_iguales <- all.equal(df_respuesta, df)
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    } else {
        print("Vuélvelo a intentar :)")
    }
    response <- POST(
        url = "https://calificar-r-435015279585.us-central1.run.app",
        body = list(JPY_SESSION_NAME = "Notebook47", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}

guardar_48 <- function(df) {
    r1_calidad_modelo <- -0.0053
    r2_sexo_sig <- FALSE
    r3_coef_edad <- -0.0480
    r4_impacto_dominante <- "edad"
    df_respuesta <- data.frame(
        item = c("bondad_ajuste", "significancia_sexo", "efecto_edad", "lider_predictor"),
        valor = c(as.character(r1_calidad_modelo),
                as.character(r2_sexo_sig),
                as.character(r3_coef_edad),
                r4_impacto_dominante)
    )   
    son_iguales <- all.equal(df_respuesta, df)
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    } else {
        print("Vuélvelo a intentar :)")
    }
    response <- POST(
        url = "https://calificar-r-435015279585.us-central1.run.app",
        body = list(JPY_SESSION_NAME = "Notebook48", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}

guardar_49 <- function(df) {
    r1_calidad_modelo <- -0.0053
    r2_sexo_sig <- FALSE
    r3_coef_edad <- -0.0480
    r4_impacto_dominante <- "edad"
    df_respuesta <- data.frame(
        item = c("bondad_ajuste", "significancia_sexo", "efecto_edad", "lider_predictor"),
        valor = c(as.character(r1_calidad_modelo),
                as.character(r2_sexo_sig),
                as.character(r3_coef_edad),
                r4_impacto_dominante)
    )   
    son_iguales <- all.equal(df_respuesta, df)
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    } else {
        print("Vuélvelo a intentar :)")
    }
    response <- POST(
        url = "https://calificar-r-435015279585.us-central1.run.app",
        body = list(JPY_SESSION_NAME = "Notebook49", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}

guardar_50 <- function(df) {
    r1_calidad_modelo <- -0.0053
    r2_sexo_sig <- FALSE
    r3_coef_edad <- -0.0480
    r4_impacto_dominante <- "edad"
    df_respuesta <- data.frame(
        item = c("bondad_ajuste", "significancia_sexo", "efecto_edad", "lider_predictor"),
        valor = c(as.character(r1_calidad_modelo),
                as.character(r2_sexo_sig),
                as.character(r3_coef_edad),
                r4_impacto_dominante)
    )   
    son_iguales <- all.equal(df_respuesta, df)
    if (son_iguales) {
        print("Bien hecho :D")
        calificacion <- 1
    } else {
        print("Vuélvelo a intentar :)")
    }
    response <- POST(
        url = "https://calificar-r-435015279585.us-central1.run.app",
        body = list(JPY_SESSION_NAME = "Notebook50", usuario = Sys.getenv("JUPYTERHUB_USER"), calificacion = calificacion),
        encode = "json" # Automatically sets Content-Type to application/json
    )
    print("Calificación guardada")
    content(response, "parsed")
}