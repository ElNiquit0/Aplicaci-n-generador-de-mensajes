import tkinter as tk
from tkinter import messagebox
import sys


def regresar_a_seleccion(ventana_actual):
    ventana_actual.destroy()  
    mostrar_ventana_seleccion()  

#VENTANAS
def ventana_WhatsApp():
    ventana_whatsapp = tk.Toplevel()
    def generar_whatsapp():
        nombre_solicitante = solicitante_entry.get()
        nombre_practicantes = practicantes_entry.get()
        horario_lunes = lunes_entry.get()
        horario_martes = martes_entry.get()
        horario_miercoles = miercoles_entry.get()
        horario_jueves = jueves_entry.get()

        mensaje_text_whatsapp.delete(1.0, tk.END)
        mensaje_whatsapp = (f"Estimado/a {nombre_solicitante}, le escribe {nombre_practicantes}, practicantes del Consultorio Jurídico Gratuito de la USFQ.\n"
                        "Con este mensaje se pretende informarle que su solicitud ha sido recibida.\n"
                        "  \n"
                        "De acuerdo con la normativa interna, debemos entrevistarle en máximo 10 días contados a partir de hoy. Contamos con la disponibilidad para la entrevista en los siguiente horarios:\n"
                        "   \n"
                        f"LUNES: {horario_lunes}\n"
                        f"MARTES {horario_martes}\n"
                        f"MIERCOLES: {horario_miercoles}\n"
                        f"JUEVES: {horario_jueves}\n"
                        "   \n"
                        "Por lo que le pedimos que nos informe cuándo es para usted más conveniente de asistir. La ubicación del consultorio es en Cumbayá, Paseo San Francisco, el Edificio Hayek Piso 1, oficina H014. Para la entrevista, le solicitamos que asista con los siguientes documentos:\n"
                        "   \n"
                        "1.- Copia de su cédula\n"
                        "2.- Historial de aportaciones al IESS y/o 3 últimos roles de pago. En caso de no estar afiliado certificado de cesantía o de no estar afiliado.\n"
                        "En caso de contar con RUC o RIMPE activo, proporcionar la última declaración al SRI.\n"
                        "   \n"
                        "Después de la entrevista y la respectiva revisión de los datos proporcionados, se le enviará el pedido de la documentación necesaria para el proceso que usted requiere.\n"
                        "   \n"
                        "Es importante recalcar que usted tiene 30 días calendario para remitir dicha documentación debido a que, si no entrega los documentos, se archivará la solicitud.\n"
                        "Esto, en virtud de que manejamos un alto número de solicitudes y es importante para nosotros atender la mayor cantidad de casos posibles, por lo que debemos actuar de forma eficiente.\n"
                        "   \n"
                        "Quedamos pendientes a cualquier duda al respecto.")
                         
        mensaje_text_whatsapp.insert(tk.END, mensaje_whatsapp)
        
       
        
    ventana_whatsapp.title("Mensaje de WhatsApp")
    ventana_whatsapp.geometry("1080x1080")
   

    tk.Label(ventana_whatsapp, text="Coloque los nombres de los practicante (Nombre y Apellido)").pack(pady=5)
    practicantes_entry = tk.Entry(ventana_whatsapp)
    practicantes_entry.pack(pady=10)

    tk.Label(ventana_whatsapp, text="Coloque los nombres del solicitante (Nombre y Apellido)").pack(pady=5)
    solicitante_entry = tk.Entry(ventana_whatsapp)
    solicitante_entry.pack(pady=10)


    tk.Label(ventana_whatsapp, text="Coloque su horario de lunes (Ej. 12:00am - 13:20pm)").pack(pady=5)
    lunes_entry = tk.Entry(ventana_whatsapp)
    lunes_entry.pack(pady=10)

    tk.Label(ventana_whatsapp, text="Coloque su horario del martes (Ej. 12:00am - 13:20pm)").pack(pady=5)
    martes_entry = tk.Entry(ventana_whatsapp)
    martes_entry.pack(pady=10)

    tk.Label(ventana_whatsapp, text="Coloque su horario del miercoles (Ej. 12:00am - 13:20pm)").pack(pady=5)
    miercoles_entry = tk.Entry(ventana_whatsapp)
    miercoles_entry.pack(pady=10)

    tk.Label(ventana_whatsapp, text="Coloque su horario del jueves (Ej. 12:00am - 13:20pm)").pack(pady=5)
    jueves_entry = tk.Entry(ventana_whatsapp)
    jueves_entry.pack(pady=10)
    # botones
    tk.Button(ventana_whatsapp, text="Generar Mensaje", command=generar_whatsapp).pack(pady=10)
    tk.Button(ventana_whatsapp, text="Regresar a Selección", command=lambda: regresar_a_seleccion(ventana_whatsapp)).pack(pady=20)
 
   #caja de texto
    tk.Label(ventana_whatsapp, text="Mensaje generado:").pack(pady=5)
    mensaje_text_whatsapp = tk.Text(ventana_whatsapp, height=40, width=90)
    mensaje_text_whatsapp.pack(pady=10)

def ventana_familia():
    def abrir_ventana_caso_familia():
        caso = caso_var.get()
        if caso == "":
            messagebox.showerror("Error", "Debe seleccionar un caso.")
        else:
            ventanaf.withdraw() 
            crear_ventana_caso_elegido_familia(caso)
    def regresar_seleccion_familia(ventana_caso_familia):
        ventana_caso_familia.destroy() 
        ventanaf.deiconify()
    def crear_ventana_caso_elegido_familia(caso):
        def generar_mensaje(): 
            sys.setrecursionlimit(10000)
            try:
                #variables
                nombre_usuario = nombre_entry.get()
                genero = genero_var.get()
                estado_de_trabajo = trabajo_var.get()
                iess = iess_var.get()
                sri = sri_var.get()
                #variables condicionales
                bebe = ""
                obligado = ""
                discapacidad = ""
                discapacidad3 = ""
                pension = ""
                alimentos = ""
                supa = ""
                ausencia = ""
                mayor = ""
                pension_divorcio = ""
                hijos_causal = ""
                causal_proceso = ""
                if int(caso[0]) == 4:
                    bebe = bebe_var.get()
                elif int(caso[0]) == 5:
                    obligado = obligado_var.get()
                elif int(caso[0]) == 2:
                    discapacidad = discapacidad_var.get()
                elif int(caso[0]) == 3:
                    discapacidad3 = discapacidad3_var.get()
                elif int(caso[0]) == 6:
                    pension = pension_var.get()
                elif int(caso[0]) == 7:
                    alimentos = alimentos_var.get()
                    supa = supa_var.get()
                elif int(caso[0]) == 9:
                    ausencia = ausencia_var.get()
                elif caso == "13.- Divorcio por mutuo consentimiento sin hijos dependientes":
                    mayor = mayor_var.get()
                elif caso == "14.- Divorcio por mutuo consentimiento con hijos dependientes":
                    pension_divorcio = pension_divorcio_var.get()
                elif caso == "16.- Divorcio por causal sin hijos dependientes":
                    hijos_causal = hijos_causal_var.get()
                elif caso == "17.- Divorcio por causal con hijos dependientes":
                    causal_proceso = causal_proceso_var.get()
                
                #logica
                mensaje_text_familia.delete(1.0, tk.END)
                if (caso == "1.- Familia iniciado" and genero == "M" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si"):
                    mensaje_familia = (f"Estimado solicitante {nombre_usuario}, le informamos que, tras la entrevista preliminar, su causa ha pasado a la siguiente etapa. Para continuar y obtener el patrocinio legal, necesitaremos la siguiente documentación\n"
                        "   \n"
                        "1.- Copia de cédula vigente\n"
                        "2.- Certificado de afiliación IESS e historial de aportaciones\n"
                        "3.- Certificado de nacimiento de todos sus hijos (vigente)\n"
                        "4.- Número del proceso\n"
                        "5.- Copias simples del proceso\n"
                        "6.- Croquis y dirección exacta del domicilio del demandado.\n"
                        "   \n"
                        "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                        "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                        "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "1.- Familia iniciado" == 1 and genero == "F" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si"):
                    mensaje_familia = (f"Estimada solicitante {nombre_usuario}, le informamos que, tras la entrevista preliminar, su causa de proceso de familia iniciado ha pasado a la siguiente etapa. Para continuar y obtener el patrocinio legal, necesitaremos la siguiente documentación\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de no afiliación IESS. Última declaración de impuestos ante el Servicio de Rentas Internas u otros documentos que justifiquen ingresos\n"
                            "3.- Certificado de nacimiento de todos sus hijos (vigente)\n"
                            "4.- Número del proceso\n"
                            "5.- Copias simples del proceso en caso de tenerlas. Si debe presentar la contestación requeriremos las copias de la demanda íntegra, así como los anexos\n"
                            "6.- Si el caso está en etapa de citación, y dicha solemnidad no se ha logrado, pedir croquis y dirección exacta del domicilio de la persona a la que se va a demandar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, calle secundaria y código postal (de ser posible ubicación GPS).\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "1.- Familia iniciado" == 1 and genero == "M" and iess == "No" and sri == "Si" and estado_de_trabajo == "No"):
                    mensaje_familia = (f"Estimado solicitante {nombre_usuario}, le informamos que, tras la entrevista preliminar, su causa de proceso de familia iniciado ha pasado a la siguiente etapa. Para continuar y obtener el patrocinio legal, necesitaremos la siguiente documentación\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de no afiliación IESS. Última declaración de impuestos ante el Servicio de Rentas Internas u otros documentos que justifiquen ingresos\n"
                            "3.- Certificado de nacimiento de todos sus hijos (vigente)\n"
                            "4.- Número del proceso\n"
                            "5.- Copias simples del proceso en caso de tenerlas. Si debe presentar la contestación requeriremos las copias de la demanda íntegra, así como los anexos\n"
                            "6.- Si el caso está en etapa de citación, y dicha solemnidad no se ha logrado, pedir croquis y dirección exacta del domicilio de la persona a la que se va a demandar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, calle secundaria y código postal (de ser posible ubicación GPS).\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "1.- Familia iniciado" == 1 and genero == "F" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si"):
                    mensaje_familia = (f"Estimada solicitante {nombre_usuario}, le informamos que, tras la entrevista preliminar, su causa de proceso de familia iniciado ha pasado a la siguiente etapa. Para continuar y obtener el patrocinio legal, necesitaremos la siguiente documentación\n"
                        "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de afiliación IESS. Historias de aportaciones al IESS y tres últimos roles de pago\n"
                            "3.- Certificado de nacimiento de todos sus hijos (vigente)\n"
                            "4.- Número del proceso\n"
                            "5.- Copias simples del proceso en caso de tenerlas. Si debe presentar la contestación requeriremos las copias de la demanda íntegra, así como los anexos\n"
                            "6.- Si el caso está en etapa de citación, y dicha solemnidad no se ha logrado, pedir croquis y dirección exacta del domicilio de la persona a la que se va a demandar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, calle secundaria y código postal (de ser posible ubicación GPS).\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "1.- Familia iniciado" == 1 and genero == "F" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si"):
                    mensaje_familia = (f"Estimada solicitante {nombre_usuario}, le informamos que, tras la entrevista preliminar, su causa de proceso de familia iniciado ha pasado a la siguiente etapa. Para continuar y obtener el patrocinio legal, necesitaremos la siguiente documentación\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de no afiliación IESS. Última declaración de impuestos ante el Servicio de Rentas Internas u otros documentos que justifiquen ingresos\n"
                            "3.- Certificado de nacimiento de todos sus hijos (vigente)\n"
                            "4.- Número del proceso\n"
                            "5.- Copias simples del proceso en caso de tenerlas. Si debe presentar la contestación requeriremos las copias de la demanda íntegra, así como los anexos\n"
                            "6.- Si el caso está en etapa de citación, y dicha solemnidad no se ha logrado, pedir croquis y dirección exacta del domicilio de la persona a la que se va a demandar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, calle secundaria y código postal (de ser posible ubicación GPS).\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "1.- Familia iniciado" == 1 and genero == "F" and iess == "No" and sri == "Si" and estado_de_trabajo == "No"):
                    mensaje_familia = (f"Estimada solicitante {nombre_usuario}, le informamos que, tras la entrevista preliminar, su causa de proceso de familia iniciado ha pasado a la siguiente etapa. Para continuar y obtener el patrocinio legal, necesitaremos la siguiente documentación\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de no afiliación IESS. Última declaración de impuestos ante el Servicio de Rentas Internas u otros documentos que justifiquen ingresos\n"
                            "3.- Certificado de nacimiento de todos sus hijos (vigente)\n"
                            "4.- Número del proceso\n"
                            "5.- Copias simples del proceso en caso de tenerlas. Si debe presentar la contestación requeriremos las copias de la demanda íntegra, así como los anexos\n"
                            "6.- Si el caso está en etapa de citación, y dicha solemnidad no se ha logrado, pedir croquis y dirección exacta del domicilio de la persona a la que se va a demandar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, calle secundaria y código postal (de ser posible ubicación GPS).\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "1.- Familia iniciado" == 1 and genero == "M" and iess == "No" and sri == "No" and estado_de_trabajo == "No"):
                    mensaje_familia = (f"Estimado solicitante {nombre_usuario}, le informamos que, tras la entrevista preliminar, su causa de proceso de familia iniciado ha pasado a la siguiente etapa. Para continuar y obtener el patrocinio legal, necesitaremos la siguiente documentación\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de no afiliación IESS.\n"
                            "3.- Certificado de nacimiento de todos sus hijos (vigente)\n"
                            "4.- Número del proceso\n"
                            "5.- Copias simples del proceso en caso de tenerlas. Si debe presentar la contestación requeriremos las copias de la demanda íntegra, así como los anexos\n"
                            "6.- Si el caso está en etapa de citación, y dicha solemnidad no se ha logrado, pedir croquis y dirección exacta del domicilio de la persona a la que se va a demandar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, calle secundaria y código postal (de ser posible ubicación GPS).\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "1.- Familia iniciado" == 1 and genero == "F" and iess == "No" and sri == "No" and estado_de_trabajo == "No"):
                    mensaje_familia = (f"Estimada solicitante {nombre_usuario}, le informamos que, tras la entrevista preliminar, su causa de proceso de familia iniciado ha pasado a la siguiente etapa. Para continuar y obtener el patrocinio legal, necesitaremos la siguiente documentación\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de no afiliación IESS.\n"
                            "3.- Certificado de nacimiento de todos sus hijos (vigente)\n"
                            "4.- Número del proceso\n"
                            "5.- Copias simples del proceso en caso de tenerlas. Si debe presentar la contestación requeriremos las copias de la demanda íntegra, así como los anexos\n"
                            "6.- Si el caso está en etapa de citación, y dicha solemnidad no se ha logrado, pedir croquis y dirección exacta del domicilio de la persona a la que se va a demandar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, calle secundaria y código postal (de ser posible ubicación GPS).\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")    
                #FAMILIA NO INICIADO CON DSCAPACIDAD    
                elif (int(caso[0]) == 2 and genero == "M" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si" and discapacidad == "Si"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio.\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de afiliación IESS e historial de aportaciones\n"
                            "3.- Certificado de nacimiento de todos sus hijos (vigente)\n"
                            "4.- Generales de ley de la persona a quien se va a demandar;\n"
                            "5.- Croquis y dirección exacta del domicilio/lugar de trabajo de la persona a la que se va a demandar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS).\n"
                            "6.- Certificado de cuenta bancaria que va a ser vinculada al SUPA.\n "
                            "7.- Certificado de identidad y estado civil donde consta la discapacidad registrada. Si no tiene la discapacidad registrada, pedir certificado de discapacidad emitido por el Ministerio de Salud Pública.\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 2 and genero == "F" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si" and discapacidad == "Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio.\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de afiliación IESS e historial de aportaciones\n"
                            "3.- Certificado de nacimiento de todos sus hijos (vigente)\n"
                            "4.- Generales de ley de la persona a quien se va a demandar;\n"
                            "5.- Croquis y dirección exacta del domicilio/lugar de trabajo de la persona a la que se va a demandar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                            "6.- Certificado de cuenta bancaria que va a ser vinculada al SUPA\n"
                            "7.- Certificado de identidad y estado civil donde consta la discapacidad registrada. Si no tiene la discapacidad registrada, pedir certificado de discapacidad emitido por el Ministerio de Salud Pública.\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 2 and genero == "M" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si" and discapacidad == "Si"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio.\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de no afiliación IESS. Última declaración de impuestos ante el Servicio de Rentas Internas u otros documentos que justifiquen ingresos\n"
                            "3.- Certificado de nacimiento de todos sus hijos (vigente)\n"
                            "4.- Generales de ley de la persona a quien se va a demandar;\n"
                            "5.- Croquis y dirección exacta del domicilio/lugar de trabajo de la persona a la que se va a demandar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                            "6.- Certificado de cuenta bancaria que va a ser vinculada al SUPA\n"
                            "7.- Certificado de identidad y estado civil donde consta la discapacidad registrada. Si no tiene la discapacidad registrada, pedir certificado de discapacidad emitido por el Ministerio de Salud Pública.\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 2 and genero == "F" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si" and discapacidad == "Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio.\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de no afiliación IESS. Última declaración de impuestos ante el Servicio de Rentas Internas u otros documentos que justifiquen ingresos\n"
                            "3.- Certificado de nacimiento de todos sus hijos (vigente)\n"
                            "4.- Generales de ley de la persona a quien se va a demandar;\n"
                            "5.- Croquis y dirección exacta del domicilio/lugar de trabajo de la persona a la que se va a demandar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                            "6.- Certificado de cuenta bancaria que va a ser vinculada al SUPA\n"
                            "7.- Certificado de identidad y estado civil donde consta la discapacidad registrada. Si no tiene la discapacidad registrada, pedir certificado de discapacidad emitido por el Ministerio de Salud Pública.\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 2 and genero == "M" and iess == "Si" and sri == "No" and estado_de_trabajo == "No" and discapacidad == "Si"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio.\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de no afiliación IESS e historial de aportaciones.\n"
                            "3.- Certificado de nacimiento de todos sus hijos (vigente)\n"
                            "4.- Generales de ley de la persona a quien se va a demandar;\n"
                            "5.- Croquis y dirección exacta del domicilio/lugar de trabajo de la persona a la que se va a demandar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                            "6.- Certificado de cuenta bancaria que va a ser vinculada al SUPA\n"
                            "7.- Certificado de identidad y estado civil donde consta la discapacidad registrada del titular del derecho. Si no tiene la discapacidad registrada, pedir certificado de discapacidad emitido por el Ministerio de Salud Pública.\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 2 and genero == "F" and iess == "Si" and sri == "No" and estado_de_trabajo == "No" and discapacidad == "Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio.\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de afiliación IESS e historial de aportaciones.\n"
                            "3.- Certificado de nacimiento de todos sus hijos (vigente)\n"
                            "4.- Generales de ley de la persona a quien se va a demandar;\n"
                            "5.- Croquis y dirección exacta del domicilio/lugar de trabajo de la persona a la que se va a demandar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                            "6.- Certificado de cuenta bancaria que va a ser vinculada al SUPA\n"
                            "7.- Certificado de identidad y estado civil donde consta la discapacidad registrada del titular del derecho. Si no tiene la discapacidad registrada, pedir certificado de discapacidad emitido por el Ministerio de Salud Pública.\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 2 and genero == "M" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and discapacidad == "Si"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio.\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de no afiliación IESS. Documentos que justifiquen \n"  # DOCS QUE JUSTIFIQUEN 
                            "3.- Certificado de nacimiento de todos sus hijos (vigente)\n"
                            "4.- Generales de ley de la persona a quien se va a demandar;\n"
                            "5.- Croquis y dirección exacta del domicilio/lugar de trabajo de la persona a la que se va a demandar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                            "6.- Certificado de cuenta bancaria que va a ser vinculada al SUPA\n"
                            "7.- Certificado de identidad y estado civil donde consta la discapacidad registrada del titular del derecho. Si no tiene la discapacidad registrada, pedir certificado de discapacidad emitido por el Ministerio de Salud Pública.\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 2 and genero == "F" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and discapacidad == "Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio.\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de no afiliación IESS. Documentos que justifiquen \n"  # DOCS QUE JUSTIFIQUEN 
                            "3.- Certificado de nacimiento de todos sus hijos (vigente)\n"
                            "4.- Generales de ley de la persona a quien se va a demandar;\n"
                            "5.- Croquis y dirección exacta del domicilio/lugar de trabajo de la persona a la que se va a demandar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                            "6.- Certificado de cuenta bancaria que va a ser vinculada al SUPA\n"
                            "7.- Certificado de identidad y estado civil donde consta la discapacidad registrada del titular del derecho. Si no tiene la discapacidad registrada, pedir certificado de discapacidad emitido por el Ministerio de Salud Pública.\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                #FAMILIA NO INICIADO SIN DISCAPACIDAD
                elif (int(caso[0]) == 2 and genero == "M" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si" and discapacidad == "No"): 
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte deL Consultorio. Para ello necesitaremos que presente los siguientes documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de afiliación IESS e historial de aportaciones\n"
                            "3.- Certificado de nacimiento de todos sus hijos (vigente)\n"
                            "4.- Generales de ley de la persona a quien se va a demandar;\n"
                            "5.- Croquis y dirección exacta del domicilio/lugar de trabajo de la persona a la que se va a demandar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                            "6.- Certificado de cuenta bancaria que va a ser vinculada al SUPA \n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 2 and genero == "F" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si" and discapacidad == "No"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte deL Consultorio. Para ello necesitaremos que presente los siguientes documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de afiliación IESS e historial de aportaciones\n"
                            "3.- Certificado de nacimiento de todos sus hijos (vigente)\n"
                            "4.- Generales de ley de la persona a quien se va a demandar;\n"
                            "5.- Croquis y dirección exacta del domicilio/lugar de trabajo de la persona a la que se va a demandar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                            "6.- Certificado de cuenta bancaria que va a ser vinculada al SUPA \n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 2 and genero == "M" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si" and discapacidad == "No"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte deL Consultorio. Para ello necesitaremos que presente los siguientes documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de no afiliación IESS. Última declaración de impuestos ante el Servicio de Rentas Internas u otros documentos que justifiquen ingresos\n"
                            "3.- Certificado de nacimiento de todos sus hijos (vigente)\n"
                            "4.- Generales de ley de la persona a quien se va a demandar;\n"
                            "5.- Croquis y dirección exacta del domicilio/lugar de trabajo de la persona a la que se va a demandar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                            "6.- Certificado de cuenta bancaria que va a ser vinculada al SUPA \n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 2 and genero == "F" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si" and discapacidad == "No"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte deL Consultorio. Para ello necesitaremos que presente los siguientes documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de no afiliación IESS. Última declaración de impuestos ante el Servicio de Rentas Internas u otros documentos que justifiquen ingresos\n"
                            "3.- Certificado de nacimiento de todos sus hijos (vigente)\n"
                            "4.- Generales de ley de la persona a quien se va a demandar;\n"
                            "5.- Croquis y dirección exacta del domicilio/lugar de trabajo de la persona a la que se va a demandar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                            "6.- Certificado de cuenta bancaria que va a ser vinculada al SUPA \n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 2 and genero == "M" and iess == "Si" and sri == "No" and estado_de_trabajo == "No" and discapacidad == "No"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte deL Consultorio. Para ello necesitaremos que presente los siguientes documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de no afiliación IESS e historial de aportaciones.\n"
                            "3.- Certificado de nacimiento de todos sus hijos (vigente)\n"
                            "4.- Generales de ley de la persona a quien se va a demandar;\n"
                            "5.- Croquis y dirección exacta del domicilio/lugar de trabajo de la persona a la que se va a demandar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                            "6.- Certificado de cuenta bancaria que va a ser vinculada al SUPA \n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 2 and genero == "F" and iess == "Si" and sri == "No" and estado_de_trabajo == "No" and discapacidad == "No"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte deL Consultorio. Para ello necesitaremos que presente los siguientes documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de afiliación IESS e historial de aportaciones.\n"
                            "3.- Certificado de nacimiento de todos sus hijos (vigente)\n"
                            "4.- Generales de ley de la persona a quien se va a demandar;\n"
                            "5.- Croquis y dirección exacta del domicilio/lugar de trabajo de la persona a la que se va a demandar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                            "6.- Certificado de cuenta bancaria que va a ser vinculada al SUPA \n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 2 and genero == "M" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and discapacidad == "No"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte deL Consultorio. Para ello necesitaremos que presente los siguientes documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de no afiliación IESS. Documentos que justifiquen.\n"
                            "3.- Certificado de nacimiento de todos sus hijos (vigente)\n"
                            "4.- Generales de ley de la persona a quien se va a demandar;\n"
                            "5.- Croquis y dirección exacta del domicilio/lugar de trabajo de la persona a la que se va a demandar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                            "6.- Certificado de cuenta bancaria que va a ser vinculada al SUPA \n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 2 and genero == "F" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and discapacidad == "No"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte deL Consultorio. Para ello necesitaremos que presente los siguientes documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de no afiliación IESS. Documentos que justifiquen.\n"
                            "3.- Certificado de nacimiento de todos sus hijos (vigente)\n"
                            "4.- Generales de ley de la persona a quien se va a demandar;\n"
                            "5.- Croquis y dirección exacta del domicilio/lugar de trabajo de la persona a la que se va a demandar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                            "6.- Certificado de cuenta bancaria que va a ser vinculada al SUPA \n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                #PRESUNCI[ON] DE PATERNIDAD CON DISCAPACIDAD DEL TITULAR
                elif (int(caso[0]) == 3 and genero == "M" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si" and discapacidad3 == "Si"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de nacimiento del hijo por el cual se demanda\n"
                            "3.- Generales de la ley de la persona a quien se va a demandar\n"
                            "4.- Croquis y dirección exacta del domicilio/lugar de trabajo de la persona a la que se va a demandar: Provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria. De ser posible ubicación GPS\n"
                            "5.- Certificado de afiliación IESS y su historial de aportaciones\n"
                            "6.- Certificado de cuenta bancaria que va a ser vinculada al SUPA\n"
                            "7.- Certificado de identidad y estado civil donde conste la discapacidad registrada. En caso de no tener discapacidad registrada, pedir el certificado de discapacidad emitido por el Ministerio de Salud Pública.\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 3 and genero == "F" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si" and discapacidad3 == "Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de nacimiento del hijo por el cual se demanda\n"
                            "3.- Generales de la ley de la persona a quien se va a demandar\n"
                            "4.- Croquis y dirección exacta del domicilio/lugar de trabajo de la persona a la que se va a demandar: Provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria. De ser posible ubicación GPS\n"
                            "5.- Certificado de afiliación IESS y su historial de aportaciones\n"
                            "6.- Certificado de cuenta bancaria que va a ser vinculada al SUPA\n"
                            "7.- Certificado de identidad y estado civil donde conste la discapacidad registrada. En caso de no tener discapacidad registrada, pedir el certificado de discapacidad emitido por el Ministerio de Salud Pública.\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 3 and genero == "M" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si" and discapacidad3 == "Si"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de nacimiento del hijo por el cual se demanda\n"
                            "3.- Generales de la ley de la persona a quien se va a demandar\n"
                            "4.- Croquis y dirección exacta del domicilio/lugar de trabajo de la persona a la que se va a demandar: Provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria. De ser posible ubicación GPS\n"
                            "5.- Tres últimos roles de pago, última declaración de impuestos u otros documentos que justifiquen ingresos\n"
                            "6.- Certificado de cuenta bancaria que va a ser vinculada al SUPA\n"
                            "7.- Certificado de identidad y estado civil donde conste la discapacidad registrada. En caso de no tener discapacidad registrada, pedir el certificado de discapacidad emitido por el Ministerio de Salud Pública.\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 3 and genero == "F" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si" and discapacidad3 == "Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de nacimiento del hijo por el cual se demanda\n"
                            "3.- Generales de la ley de la persona a quien se va a demandar\n"
                            "4.- Croquis y dirección exacta del domicilio/lugar de trabajo de la persona a la que se va a demandar: Provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria. De ser posible ubicación GPS\n"
                            "5.- Tres últimos roles de pago, última declaración de impuestos u otros documentos que justifiquen ingresos\n"
                            "6.- Certificado de cuenta bancaria que va a ser vinculada al SUPA\n"
                            "7.- Certificado de identidad y estado civil donde conste la discapacidad registrada. En caso de no tener discapacidad registrada, pedir el certificado de discapacidad emitido por el Ministerio de Salud Pública.\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 3 and genero == "M" and iess == "No" and sri == "No" and estado_de_trabajo == "Si" and discapacidad3 == "Si"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de nacimiento del hijo por el cual se demanda\n"
                            "3.- Generales de la ley de la persona a quien se va a demandar\n"
                            "4.- Croquis y dirección exacta del domicilio/lugar de trabajo de la persona a la que se va a demandar: Provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria. De ser posible ubicación GPS\n"
                            "5.- Certificado de Afiliación al IESS y certificado de contribuyente del SRI\n"
                            "6.- Certificado de cuenta bancaria que va a ser vinculada al SUPA\n"
                            "7.- Certificado de identidad y estado civil donde conste la discapacidad registrada. En caso de no tener discapacidad registrada, pedir el certificado de discapacidad emitido por el Ministerio de Salud Pública.\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 3 and genero == "F" and iess == "No" and sri == "No" and estado_de_trabajo == "Si" and discapacidad3 == "Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de nacimiento del hijo por el cual se demanda\n"
                            "3.- Generales de la ley de la persona a quien se va a demandar\n"
                            "4.- Croquis y dirección exacta del domicilio/lugar de trabajo de la persona a la que se va a demandar: Provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria. De ser posible ubicación GPS\n"
                            "5.- Certificado de Afiliación al IESS y certificado de contribuyente del SRI\n"
                            "6.- Certificado de cuenta bancaria que va a ser vinculada al SUPA\n"
                            "7.- Certificado de identidad y estado civil donde conste la discapacidad registrada. En caso de no tener discapacidad registrada, pedir el certificado de discapacidad emitido por el Ministerio de Salud Pública.\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 3 and genero == "M" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and discapacidad3 == "Si"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de nacimiento del hijo por el cual se demanda\n"
                            "3.- Generales de la ley de la persona a quien se va a demandar\n"
                            "4.- Croquis y dirección exacta del domicilio/lugar de trabajo de la persona a la que se va a demandar: Provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria. De ser posible ubicación GPS\n"
                            "5.- Certificado de Afiliación al IESS y certificado de contribuyente del SRI\n"
                            "6.- Certificado de cuenta bancaria que va a ser vinculada al SUPA\n"
                            "7.- Certificado de identidad y estado civil donde conste la discapacidad registrada. En caso de no tener discapacidad registrada, pedir el certificado de discapacidad emitido por el Ministerio de Salud Pública.\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 3 and genero == "F" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and discapacidad3 == "Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de nacimiento del hijo por el cual se demanda\n"
                            "3.- Generales de la ley de la persona a quien se va a demandar\n"
                            "4.- Croquis y dirección exacta del domicilio/lugar de trabajo de la persona a la que se va a demandar: Provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria. De ser posible ubicación GPS\n"
                            "5.- Certificado de Afiliación al IESS y certificado de contribuyente del SRI\n"
                            "6.- Certificado de cuenta bancaria que va a ser vinculada al SUPA\n"
                            "7.- Certificado de identidad y estado civil donde conste la discapacidad registrada. En caso de no tener discapacidad registrada, pedir el certificado de discapacidad emitido por el Ministerio de Salud Pública.\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                #PRESUNCION DE PATERNIDAD SIN DISCAPACIDAD DEL TITULAR
                elif (int(caso[0]) == 3 and genero == "M" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si" and discapacidad3 == "No"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de nacimiento del hijo por el cual se demanda\n"
                            "3.- Generales de la ley de la persona a quien se va a demandar\n"
                            "4.- Croquis y dirección exacta del domicilio/lugar de trabajo de la persona a la que se va a demandar: Provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria. De ser posible ubicación GPS\n"
                            "5.- Certificado de afiliación IESS y su historial de aportaciones\n"
                            "6.- Certificado de cuenta bancaria que va a ser vinculada al SUPA\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 3 and genero == "F" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si" and discapacidad3 == "No"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de nacimiento del hijo por el cual se demanda\n"
                            "3.- Generales de la ley de la persona a quien se va a demandar\n"
                            "4.- Croquis y dirección exacta del domicilio/lugar de trabajo de la persona a la que se va a demandar: Provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria. De ser posible ubicación GPS\n"
                            "5.- Certificado de afiliación IESS y su historial de aportaciones\n"
                            "6.- Certificado de cuenta bancaria que va a ser vinculada al SUPA\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 3 and genero == "M" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si" and discapacidad3 == "No"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de nacimiento del hijo por el cual se demanda\n"
                            "3.- Generales de la ley de la persona a quien se va a demandar\n"
                            "4.- Croquis y dirección exacta del domicilio/lugar de trabajo de la persona a la que se va a demandar: Provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria. De ser posible ubicación GPS\n"
                            "5.- Tres últimos roles de pago, última declaración de impuestos u otros documentos que justifiquen ingresos\n"
                            "6.- Certificado de cuenta bancaria que va a ser vinculada al SUPA\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 3 and genero == "F" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si" and discapacidad3 == "No"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de nacimiento del hijo por el cual se demanda\n"
                            "3.- Generales de la ley de la persona a quien se va a demandar\n"
                            "4.- Croquis y dirección exacta del domicilio/lugar de trabajo de la persona a la que se va a demandar: Provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria. De ser posible ubicación GPS\n"
                            "5.- Tres últimos roles de pago, última declaración de impuestos u otros documentos que justifiquen ingresos\n"
                            "6.- Certificado de cuenta bancaria que va a ser vinculada al SUPA\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 3 and genero == "M" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and discapacidad3 == "No"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de nacimiento del hijo por el cual se demanda\n"
                            "3.- Generales de la ley de la persona a quien se va a demandar\n"
                            "4.- Croquis y dirección exacta del domicilio/lugar de trabajo de la persona a la que se va a demandar: Provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria. De ser posible ubicación GPS\n"
                            "5.- Certificado de Afiliación al IESS y certificado de contribuyente del SRI\n"
                            "6.- Certificado de cuenta bancaria que va a ser vinculada al SUPA\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 3 and genero == "F" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and discapacidad3 == "No"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de nacimiento del hijo por el cual se demanda\n"
                            "3.- Generales de la ley de la persona a quien se va a demandar\n"
                            "4.- Croquis y dirección exacta del domicilio/lugar de trabajo de la persona a la que se va a demandar: Provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria. De ser posible ubicación GPS\n"
                            "5.- Certificado de Afiliación al IESS y certificado de contribuyente del SRI\n"
                            "6.- Certificado de cuenta bancaria que va a ser vinculada al SUPA\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 3 and genero == "M" and iess == "No" and sri == "No" and estado_de_trabajo == "Si" and discapacidad3 == "No"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de nacimiento del hijo por el cual se demanda\n"
                            "3.- Generales de la ley de la persona a quien se va a demandar\n"
                            "4.- Croquis y dirección exacta del domicilio/lugar de trabajo de la persona a la que se va a demandar: Provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria. De ser posible ubicación GPS\n"
                            "5.- Certificado de afiliación IESS y su historial de aportaciones\n"
                            "6.- Certificado de cuenta bancaria que va a ser vinculada al SUPA\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 3 and genero == "F" and iess == "No" and sri == "No" and estado_de_trabajo == "Si" and discapacidad3 == "No"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de nacimiento del hijo por el cual se demanda\n"
                            "3.- Generales de la ley de la persona a quien se va a demandar\n"
                            "4.- Croquis y dirección exacta del domicilio/lugar de trabajo de la persona a la que se va a demandar: Provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria. De ser posible ubicación GPS\n"
                            "5.- Certificado de afiliación IESS y su historial de aportaciones\n"
                            "6.- Certificado de cuenta bancaria que va a ser vinculada al SUPA\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")   
                #ALIMENTOS MUJER EMBARAZADA CON BEBE NACIDO
                elif (int(caso[0]) == 4 and genero == "F" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si" and bebe == "Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de afiliación IESS. Historias de aportaciones al IESS y tres últimos roles de pago\n"
                            "3.- Partida íntegra de matrimonio vigente (No el certificado)\n"
                            "4.- Certificado médico de embarazo otorgado por IESS / institución de la salud validado por el Ministerio de Salud Pública\n"
                            "5.- Certificado de nacimiento vigente del bebé\n"
                            "6.- Generales de ley de la persona a quien se va a demandar (Nombre, edad, número de cédula, estado civil, etc.)\n"
                            "7.- Croquis y dirección exacta del domicilio de la persona a la que se va a demandar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, calle secundaria y código postal (de ser posible ubicación GPS).\n"
                            "8.- Fotografías materializadas de actora y demandado juntos, con el fin de probar existencia de relación (opcional).\n"
                            "9.- Certificado de cuenta bancaria que va a ser vinculada al SUPA\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 4 and genero == "F" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si" and bebe == "Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de no afiliación IESS. Última declaración de impuestos ante el Servicio de Rentas Internas u otros documentos que justifiquen ingresos\n"
                            "3.- Partida íntegra de matrimonio vigente (No el certificado)\n"
                            "4.- Certificado médico de embarazo otorgado por IESS / institución de la salud validado por el Ministerio de Salud Pública\n"
                            "5.- Certificado de nacimiento vigente del bebé\n"
                            "6.- Generales de ley de la persona a quien se va a demandar (Nombre, edad, número de cédula, estado civil, etc.)\n"
                            "7.- Croquis y dirección exacta del domicilio de la persona a la que se va a demandar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, calle secundaria y código postal (de ser posible ubicación GPS).\n"
                            "8.- Fotografías materializadas de actora y demandado juntos, con el fin de probar existencia de relación (opcional).\n"
                            "9.- Certificado de cuenta bancaria que va a ser vinculada al SUPA\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 4 and genero == "F" and iess == "No" and sri == "Si" and estado_de_trabajo == "No" and bebe == "Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de no afiliación IESS. Última declaración de impuestos ante el Servicio de Rentas Internas u otros documentos que justifiquen ingresos\n"
                            "3.- Partida íntegra de matrimonio vigente (No el certificado)\n"
                            "4.- Certificado médico de embarazo otorgado por IESS / institución de la salud validado por el Ministerio de Salud Pública\n"
                            "5.- Certificado de nacimiento vigente del bebé\n"
                            "6.- Generales de ley de la persona a quien se va a demandar (Nombre, edad, número de cédula, estado civil, etc.)\n"
                            "7.- Croquis y dirección exacta del domicilio de la persona a la que se va a demandar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, calle secundaria y código postal (de ser posible ubicación GPS).\n"
                            "8.- Fotografías materializadas de actora y demandado juntos, con el fin de probar existencia de relación (opcional).\n"
                            "9.- Certificado de cuenta bancaria que va a ser vinculada al SUPA\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 4 and genero == "F" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si" and bebe == "Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de afiliación IESS. Historias de aportaciones al IESS y tres últimos roles de pago\n"
                            "3.- Partida íntegra de matrimonio vigente (No el certificado)\n"
                            "4.- Certificado médico de embarazo otorgado por IESS / institución de la salud validado por el Ministerio de Salud Pública\n"
                            "5.- Certificado de nacimiento vigente del bebé\n"
                            "6.- Generales de ley de la persona a quien se va a demandar (Nombre, edad, número de cédula, estado civil, etc.)\n"
                            "7.- Croquis y dirección exacta del domicilio de la persona a la que se va a demandar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, calle secundaria y código postal (de ser posible ubicación GPS).\n"
                            "8.- Fotografías materializadas de actora y demandado juntos, con el fin de probar existencia de relación (opcional).\n"
                            "9.- Certificado de cuenta bancaria que va a ser vinculada al SUPA\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                #ALIMENTOS MUJER EMBARAZADA CON BEBE NO NACIDO
                elif (int(caso[0]) == 4 and genero == "F" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si" and bebe == "No"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de afiliación IESS. Historias de aportaciones al IESS y tres últimos roles de pago\n"
                            "3.- Partida íntegra de matrimonio vigente (No el certificado)\n"
                            "4.- Certificado médico de embarazo otorgado por IESS / institución de la salud validado por el Ministerio de Salud Pública\n"
                            "5.- Generales de ley de la persona a quien se va a demandar (Nombre, edad, número de cédula, estado civil, etc.)\n"
                            "6.- Croquis y dirección exacta del domicilio de la persona a la que se va a demandar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, calle secundaria y código postal (de ser posible ubicación GPS).\n"
                            "7.- Fotografías materializadas de actora y demandado juntos, con el fin de probar existencia de relación (opcional).\n"
                            "8.- Certificado de cuenta bancaria que va a ser vinculada al SUPA\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 4 and genero == "F" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si" and bebe == "No"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de no afiliación IESS. Última declaración de impuestos ante el Servicio de Rentas Internas u otros documentos que justifiquen ingresos\n"
                            "3.- Partida íntegra de matrimonio vigente (No el certificado)\n"
                            "4.- Certificado médico de embarazo otorgado por IESS / institución de la salud validado por el Ministerio de Salud Pública\n"
                            "5.- Generales de ley de la persona a quien se va a demandar (Nombre, edad, número de cédula, estado civil, etc.)\n"
                            "6.- Croquis y dirección exacta del domicilio de la persona a la que se va a demandar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, calle secundaria y código postal (de ser posible ubicación GPS).\n"
                            "7.- Fotografías materializadas de actora y demandado juntos, con el fin de probar existencia de relación (opcional).\n"
                            "8.- Certificado de cuenta bancaria que va a ser vinculada al SUPA\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 4 and genero == "F" and iess == "No" and sri == "Si" and estado_de_trabajo == "No" and bebe == "No"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de no afiliación IESS. Última declaración de impuestos ante el Servicio de Rentas Internas u otros documentos que justifiquen ingresos\n"
                            "3.- Partida íntegra de matrimonio vigente (No el certificado)\n"
                            "4.- Certificado médico de embarazo otorgado por IESS / institución de la salud validado por el Ministerio de Salud Pública\n"
                            "5.- Generales de ley de la persona a quien se va a demandar (Nombre, edad, número de cédula, estado civil, etc.)\n"
                            "6.- Croquis y dirección exacta del domicilio de la persona a la que se va a demandar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, calle secundaria y código postal (de ser posible ubicación GPS).\n"
                            "7.- Fotografías materializadas de actora y demandado juntos, con el fin de probar existencia de relación (opcional).\n"
                            "8.- Certificado de cuenta bancaria que va a ser vinculada al SUPA\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 4 and genero == "F" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si" and bebe == "No"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de afiliación IESS. Historias de aportaciones al IESS y tres últimos roles de pago\n"
                            "3.- Partida íntegra de matrimonio vigente (No el certificado)\n"
                            "4.- Certificado médico de embarazo otorgado por IESS / institución de la salud validado por el Ministerio de Salud Pública\n"
                            "5.- Generales de ley de la persona a quien se va a demandar (Nombre, edad, número de cédula, estado civil, etc.)\n"
                            "6.- Croquis y dirección exacta del domicilio de la persona a la que se va a demandar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, calle secundaria y código postal (de ser posible ubicación GPS).\n"
                            "7.- Fotografías materializadas de actora y demandado juntos, con el fin de probar existencia de relación (opcional).\n"
                            "8.- Certificado de cuenta bancaria que va a ser vinculada al SUPA\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")    
                #PROCESO DE COBRO DE DEUDA DE PENSIONES ART 137 (SOLICITANTE ES PARTE OBLIGADA)
                elif (int(caso[0]) == 5 and genero == "M" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si" and obligado == "Si"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de nacimiento original de todos sus hijos\n"
                            "3.- Número de proceso\n"
                            "4.- Certificado de afiliación IESS e historial de aportaciones\n"
                            "5.- Propuesta de pago, misma que debe ser coherente con el monto adeudado, procurando que el abono inicial sea de al menos el 30% del total adeudado\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 5 and genero == "F" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si" and obligado == "Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                    "   \n"
                    "1.- Copia de cédula vigente\n"
                    "2.- Certificado de nacimiento original de todos sus hijos\n"
                    "3.- Número de proceso\n"
                    "4.- Certificado de afiliación IESS e historial de aportaciones\n"
                    "5.- Propuesta de pago, misma que debe ser coherente con el monto adeudado, procurando que el abono inicial sea de al menos el 30% del total adeudado\n"
                    "   \n"
                    "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                    "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                    "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 5 and genero == "M" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si" and obligado == "Si"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de nacimiento original de todos sus hijos\n"
                            "3.- Número de proceso\n"
                            "4.- Certificado de no afiliación IESS. Última declaración de impuestos ante el Servicio de Rentas Internas u otros documentos que justifiquen ingresos\n"
                            "5.- Propuesta de pago, misma que debe ser coherente con el monto adeudado, procurando que el abono inicial sea de al menos el 30% del total adeudado\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 5 and genero == "F" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si" and obligado == "Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de nacimiento original de todos sus hijos\n"
                            "3.- Número de proceso\n"
                            "4.- Certificado de no afiliación IESS. Última declaración de impuestos ante el Servicio de Rentas Internas u otros documentos que justifiquen ingresos\n"
                            "5.- Propuesta de pago, misma que debe ser coherente con el monto adeudado, procurando que el abono inicial sea de al menos el 30% del total adeudado\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 5 and genero == "F" and iess == "Si" and sri == "No" and estado_de_trabajo == "No" and obligado == "Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de nacimiento original de todos sus hijos\n"
                            "3.- Número de proceso\n"
                            "4.- Certificado de no afiliación IESS. Última declaración de impuestos ante el Servicio de Rentas Internas u otros documentos que justifiquen ingresos\n"
                            "5.- Propuesta de pago, misma que debe ser coherente con el monto adeudado, procurando que el abono inicial sea de al menos el 30% del total adeudado\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 5 and genero == "F" and iess == "Si" and sri == "No" and estado_de_trabajo == "No" and obligado == "Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de nacimiento original de todos sus hijos\n"
                            "3.- Número de proceso\n"
                            "4.- Certificado de no afiliación IESS. Última declaración de impuestos ante el Servicio de Rentas Internas u otros documentos que justifiquen ingresos\n"
                            "5.- Propuesta de pago, misma que debe ser coherente con el monto adeudado, procurando que el abono inicial sea de al menos el 30% del total adeudado\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 5 and genero == "M" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and obligado == "Si"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de nacimiento original de todos sus hijos (vigente)\n"  # DOCS QUE JUSTIFIQUEN 
                            "3.- Número de proceso\n"
                            "4.- Certificado de no afiliación IESS. Documentos que justifiquen ingresos\n"
                            "5.- Propuesta de pago, misma que debe ser coherente con el monto adeudado, procurando que el abono inicial sea de al menos el 30% del total adeudado\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 5 and genero == "F" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and obligado == "Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de nacimiento original de todos sus hijos (vigente)\n"  # DOCS QUE JUSTIFIQUEN 
                            "3.- Número de proceso\n"
                            "4.- Certificado de no afiliación IESS. Documentos que justifiquen ingresos\n"
                            "5.- Propuesta de pago, misma que debe ser coherente con el monto adeudado, procurando que el abono inicial sea de al menos el 30% del total adeudado\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                #PROCESO DE COBRO DE DEUDA DE PENSIONES ART 137 (SOLICITANTE NO ES PARTE OBLIGADA)
                elif (int(caso[0]) == 5 and genero == "M" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si" and obligado == "No"): 
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de nacimiento original de todos sus hijos\n"
                            "3.- Número de proceso\n"
                            "4.- Certificado de afiliación IESS e historial de aportaciones\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 5 and genero == "F" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si" and obligado == "No"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de nacimiento original de todos sus hijos\n"
                            "3.- Número de proceso\n"
                            "4.- Certificado de afiliación IESS e historial de aportaciones\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 5 and genero == "M" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si" and obligado == "No"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de nacimiento original de todos sus hijos\n"
                            "3.- Número de proceso\n"
                            "4.- Certificado de no afiliación IESS. Última declaración de impuestos ante el Servicio de Rentas Internas u otros documentos que justifiquen ingresos\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 5 and genero == "F" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si" and obligado == "No"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de nacimiento original de todos sus hijos\n"
                            "3.- Número de proceso\n"
                            "4.- Certificado de no afiliación IESS. Última declaración de impuestos ante el Servicio de Rentas Internas u otros documentos que justifiquen ingresos\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 5 and genero == "M" and iess == "Si" and sri == "No" and estado_de_trabajo == "No" and obligado == "No"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de nacimiento original de todos sus hijos\n"
                            "3.- Número de proceso\n"
                            "4.- Certificado de no afiliación IESS e historial de aportaciones.\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 5 and genero == "F" and iess == "Si" and sri == "No" and estado_de_trabajo == "No" and obligado == "No"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de nacimiento original de todos sus hijos\n"
                            "3.- Número de proceso\n"
                            "4.- Certificado de no afiliación IESS e historial de aportaciones.\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 5 and genero == "M" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and obligado == "No"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de nacimiento de todos sus hijos (vigente) \n"  # DOCS QUE JUSTIFIQUEN 
                            "3.- Número de proceso\n"
                            "4.- Certificado de no afiliación IESS. Documentos que justifiquen ingresos\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 5 and genero == "F" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and obligado == "No"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de nacimiento de todos sus hijos (vigente) \n"  # DOCS QUE JUSTIFIQUEN 
                            "3.- Número de proceso\n"
                            "4.- Certificado de no afiliación IESS. Documentos que justifiquen ingresos\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")

                #EXTINCIÓN DE PENSIÓN ALIMENTICIA CON PENSIONES PENDIENTES DE PAGO
                elif (int(caso[0]) == 6 and genero == "M" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si" and pension == "Si"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de afiliación IESS e historial de aportaciones\n"
                            "3.- Copia de cédula o certificado de nacimiento del hijo de quien se va a pedir la extinción (vigente)\n"
                            "4.- Una fórmula de pago respecto de las pensiones pendientes de pago;\n"
                            "5.- Propuesta de pago, misma que debe ser coherente con el monto adeudado, procurando que el abono inicial sea de al menos el 30% del total adeudado\n"
                            "6.- Generales de ley de la persona sobre quien vamos a pedir que se extinga la pensión;\n"
                            "7.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 6 and genero == "F" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si" and pension == "Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de afiliación IESS e historial de aportaciones\n"
                            "3.- Copia de cédula o certificado de nacimiento del hijo de quien se va a pedir la extinción (vigente)\n"
                            "4.- Una fórmula de pago respecto de las pensiones pendientes de pago;\n"
                            "5.- Propuesta de pago, misma que debe ser coherente con el monto adeudado, procurando que el abono inicial sea de al menos el 30% del total adeudado\n"
                            "6.- Generales de ley de la persona sobre quien vamos a pedir que se extinga la pensión;\n"
                            "7.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 6 and genero == "M" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si" and pension == "Si"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de no afiliación IESS. Última declaración de impuestos ante el Servicio de Rentas Internas u otros documentos que justifiquen ingresos\n"
                            "3.- Copia de cédula o certificado de nacimiento del hijo de quien se va a pedir la extinción (vigente)\n"
                            "4.- Una fórmula de pago respecto de las pensiones pendientes de pago;\n"
                            "5.- Propuesta de pago, misma que debe ser coherente con el monto adeudado, procurando que el abono inicial sea de al menos el 30% del total adeudado\n"
                            "6.- Generales de ley de la persona sobre quien vamos a pedir que se extinga la pensión;\n"
                            "7.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 6 and genero == "F" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si" and pension == "Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de no afiliación IESS. Tres últimos roles de pago. Última declaración de impuestos ante el Servicio de Rentas Internas u otros documentos que justifiquen ingresos\n"
                            "3.- Copia de cédula o certificado de nacimiento del hijo de quien se va a pedir la extinción (vigente)\n"
                            "4.- Una fórmula de pago respecto de las pensiones pendientes de pago;\n"
                            "5.- Propuesta de pago, misma que debe ser coherente con el monto adeudado, procurando que el abono inicial sea de al menos el 30% del total adeudado\n"
                            "6.- Generales de ley de la persona sobre quien vamos a pedir que se extinga la pensión;\n"
                            "7.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 6 and genero == "M" and iess == "Si" and sri == "No" and estado_de_trabajo == "No" and pension == "Si"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de afiliación IESS e historial de aportaciones\n"
                            "3.- Copia de cédula o certificado de nacimiento del hijo de quien se va a pedir la extinción (vigente)\n"
                            "4.- Una fórmula de pago respecto de las pensiones pendientes de pago;\n"
                            "5.- Propuesta de pago, misma que debe ser coherente con el monto adeudado, procurando que el abono inicial sea de al menos el 30% del total adeudado\n"
                            "6.- Generales de ley de la persona sobre quien vamos a pedir que se extinga la pensión;\n"
                            "7.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 6 and genero == "F" and iess == "Si" and sri == "No" and estado_de_trabajo == "No" and pension == "Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de afiliación IESS e historial de aportaciones\n"
                            "3.- Copia de cédula o certificado de nacimiento del hijo de quien se va a pedir la extinción (vigente)\n"
                            "4.- Una fórmula de pago respecto de las pensiones pendientes de pago;\n"
                            "5.- Propuesta de pago, misma que debe ser coherente con el monto adeudado, procurando que el abono inicial sea de al menos el 30% del total adeudado\n"
                            "6.- Generales de ley de la persona sobre quien vamos a pedir que se extinga la pensión;\n"
                            "7.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 6 and genero == "M" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and pension == "Si"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de no afiliación IESS. Documentos que justifiquen ingresos si es que los tiene.\n"
                            "3.- Copia de cédula o certificado de nacimiento del hijo de quien se va a pedir la extinción (vigente)\n"
                            "4.- Una fórmula de pago respecto de las pensiones pendientes de pago;\n"
                            "5.- Propuesta de pago, misma que debe ser coherente con el monto adeudado, procurando que el abono inicial sea de al menos el 30% del total adeudado\n"
                            "6.- Generales de ley de la persona sobre quien vamos a pedir que se extinga la pensión;\n"
                            "7.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 6 and genero == "F" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and pension == "Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de no afiliación IESS. Documentos que justifiquen ingresos si es que los tiene.\n"
                            "3.- Copia de cédula o certificado de nacimiento del hijo de quien se va a pedir la extinción (vigente)\n"
                            "4.- Una fórmula de pago respecto de las pensiones pendientes de pago;\n"
                            "5.- Propuesta de pago, misma que debe ser coherente con el monto adeudado, procurando que el abono inicial sea de al menos el 30% del total adeudado\n"
                            "6.- Generales de ley de la persona sobre quien vamos a pedir que se extinga la pensión;\n"
                            "7.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                #EXTINCION DE PENSION ALIMENTICIA SIN PENSIONES PENDIENTES DE PAGO  
                elif (int(caso[0]) == 6 and genero == "M" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si" and pension == "No"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                            "   \n"
                            "1.- Copia de cédula vigente\n"
                            "2.- Certificado de afiliación IESS e historial de aportaciones\n"
                            "3.- Copia de cédula o certificado de nacimiento del hijo de quien se va a pedir la extinción (vigente)\n"
                            "4.- Propuesta de pago, misma que debe ser coherente con el monto adeudado, procurando que el abono inicial sea de al menos el 30% del total adeudado\n"
                            "5.- Generales de ley de la persona sobre quien vamos a pedir que se extinga la pensión;\n"
                            "6.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                            "   \n"
                            "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                            "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                            "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 6 and genero == "F" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si" and pension == "No"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de afiliación IESS e historial de aportaciones\n"
                                "3.- Copia de cédula o certificado de nacimiento del hijo de quien se va a pedir la extinción (vigente)\n"
                                "4.- Una fórmula de pago respecto de las pensiones pendientes de pago;\n"
                                "5.- Propuesta de pago, misma que debe ser coherente con el monto adeudado, procurando que el abono inicial sea de al menos el 30% del total adeudado\n"
                                "6.- Generales de ley de la persona sobre quien vamos a pedir que se extinga la pensión;\n"
                                "7.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n""Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 6 and genero == "M" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si" and pension == "No"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de no afiliación IESS. Última declaración de impuestos ante el Servicio de Rentas Internas u otros documentos que justifiquen ingresos\n"
                                "3.- Copia de cédula o certificado de nacimiento del hijo de quien se va a pedir la extinción (vigente)\n"
                                "4.- Propuesta de pago, misma que debe ser coherente con el monto adeudado, procurando que el abono inicial sea de al menos el 30% del total adeudado\n"
                                "5.- Generales de ley de la persona sobre quien vamos a pedir que se extinga la pensión;\n"
                                "6.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 6 and genero == "F" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si" and pension == "No"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de no afiliación IESS. Tres últimos roles de pago. Última declaración de impuestos ante el Servicio de Rentas Internas u otros documentos que justifiquen ingresos\n"
                                "3.- Copia de cédula o certificado de nacimiento del hijo de quien se va a pedir la extinción (vigente)\n"
                                "4.- Propuesta de pago, misma que debe ser coherente con el monto adeudado, procurando que el abono inicial sea de al menos el 30% del total adeudado\n"
                                "5.- Generales de ley de la persona sobre quien vamos a pedir que se extinga la pensión;\n"
                                "6.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 6 and genero == "M" and iess == "Si" and sri == "No" and estado_de_trabajo == "No" and pension == "No"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de afiliación IESS e historial de aportaciones\n"
                                "3.- Copia de cédula o certificado de nacimiento del hijo de quien se va a pedir la extinción (vigente)\n"
                                "4.- Propuesta de pago, misma que debe ser coherente con el monto adeudado, procurando que el abono inicial sea de al menos el 30% del total adeudado\n"
                                "5.- Generales de ley de la persona sobre quien vamos a pedir que se extinga la pensión;\n"
                                "6.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 6 and genero == "F" and iess == "Si" and sri == "No" and estado_de_trabajo == "No" and pension == "No"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de afiliación IESS e historial de aportaciones\n"
                                "3.- Copia de cédula o certificado de nacimiento del hijo de quien se va a pedir la extinción (vigente)\n"
                                "4.- Propuesta de pago, misma que debe ser coherente con el monto adeudado, procurando que el abono inicial sea de al menos el 30% del total adeudado\n"
                                "5.- Generales de ley de la persona sobre quien vamos a pedir que se extinga la pensión;\n"
                                "6.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 6 and genero == "M" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and pension == "No"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de no afiliación IESS. Documentos que justifiquen ingresos si es que los tiene.\n"
                                "3.- Copia de cédula o certificado de nacimiento del hijo de quien se va a pedir la extinción (vigente)\n"
                                "4.- Propuesta de pago, misma que debe ser coherente con el monto adeudado, procurando que el abono inicial sea de al menos el 30% del total adeudado\n"
                                "5.- Generales de ley de la persona sobre quien vamos a pedir que se extinga la pensión;\n"
                                "6.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 6 and genero == "F" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and pension == "No"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de no afiliación IESS. Documentos que justifiquen ingresos si es que los tiene.\n"
                                "3.- Copia de cédula o certificado de nacimiento del hijo de quien se va a pedir la extinción (vigente)\n"
                                "4.- Propuesta de pago, misma que debe ser coherente con el monto adeudado, procurando que el abono inicial sea de al menos el 30% del total adeudado\n"
                                "5.- Generales de ley de la persona sobre quien vamos a pedir que se extinga la pensión;\n"
                                "6.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")

                #Ejecucion de acta de mediacion de alimentos
                elif (int(caso[0]) == 7 and genero == "M" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si" and alimentos == "Si" and supa =="Si"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificados de nacimiento de los hijos contemplados en el acta (vigente)\n"
                                "3.- Original o copia certificada del acta de mediación, acreditación del centro de mediación y el listado de mediadores donde conste el mediador suscriptor\n"
                                "4.- Generales de ley de la persona a quien se va a demandar\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "6.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "7.- Certificado de cuenta bancaria que será vinculada al SUPA"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 7 and genero == "F" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si" and alimentos == "Si" and supa =="Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificados de nacimiento de los hijos contemplados en el acta (vigente)\n"
                                "3.- Original o copia certificada del acta de mediación, acreditación del centro de mediación y el listado de mediadores donde conste el mediador suscriptor\n"
                                "4.- Generales de ley de la persona a quien se va a demandar\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "6.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "7.- Certificado de cuenta bancaria que será vinculada al SUPA."
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 7 and genero == "M" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si" and alimentos == "Si" and supa =="Si"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificados de nacimiento de los hijos contemplados en el acta (vigente)\n"
                                "3.- Original o copia certificada del acta de mediación, acreditación del centro de mediación y el listado de mediadores donde conste el mediador suscriptor\n"
                                "4.- Generales de ley de la persona a quien se va a demandar\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "6.- Última declaraciónd e impuestos y sus tres últimos roles de pago\n"
                                "7.- Certificado de cuenta bancaria que será vinculada al SUPA."
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 7 and genero == "F" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si" and alimentos == "Si" and supa =="Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificados de nacimiento de los hijos contemplados en el acta (vigente)\n"
                                "3.- Original o copia certificada del acta de mediación, acreditación del centro de mediación y el listado de mediadores donde conste el mediador suscriptor\n"
                                "4.- Generales de ley de la persona a quien se va a demandar\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "6.- Última declaraciónd e impuestos y sus tres últimos roles de pago\n"
                                "7.- Certificado de cuenta bancaria que será vinculada al SUPA."
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 7 and genero == "M" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and alimentos == "Si" and supa =="Si"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificados de nacimiento de los hijos contemplados en el acta (vigente)\n"
                                "3.- Original o copia certificada del acta de mediación, acreditación del centro de mediación y el listado de mediadores donde conste el mediador suscriptor\n"
                                "4.- Generales de ley de la persona a quien se va a demandar\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "6.- Certificado de no afiliación al IESS\n" #Agregar nota de sacar captura de pantalla al estado de contribuyente en el SRI
                                "7.- Certificado de cuenta bancaria que será vinculada al SUPA."
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 7 and genero == "F" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and alimentos == "Si" and supa =="Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificados de nacimiento de los hijos contemplados en el acta (vigente)\n"
                                "3.- Original o copia certificada del acta de mediación, acreditación del centro de mediación y el listado de mediadores donde conste el mediador suscriptor\n"
                                "4.- Generales de ley de la persona a quien se va a demandar\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "6.- Certificado de no afiliación al IESS\n" #Agregar nota de sacar captura de pantalla al estado de contribuyente en el SRI
                                "7.- Certificado de cuenta bancaria que será vinculada al SUPA."
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 7 and genero == "M" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and alimentos == "Si" and supa =="Si"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificados de nacimiento de los hijos contemplados en el acta (vigente)\n"
                                "3.- Original o copia certificada del acta de mediación, acreditación del centro de mediación y el listado de mediadores donde conste el mediador suscriptor\n"
                                "4.- Generales de ley de la persona a quien se va a demandar\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "6.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "7.- Certificado de cuenta bancaria que será vinculada al SUPA"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 7 and genero == "F" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and alimentos == "Si" and supa =="Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificados de nacimiento de los hijos contemplados en el acta (vigente)\n"
                                "3.- Original o copia certificada del acta de mediación, acreditación del centro de mediación y el listado de mediadores donde conste el mediador suscriptor\n"
                                "4.- Generales de ley de la persona a quien se va a demandar\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "6.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "7.- Certificado de cuenta bancaria que será vinculada al SUPA"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                #Ejecucion de acta de mediacion NO alimentos
                elif (int(caso[0]) == 7 and genero == "M" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si" and alimentos == "No" and supa =="No"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificados de nacimiento de los hijos contemplados en el acta (vigente)\n"
                                "3.- Original o copia certificada del acta de mediación, acreditación del centro de mediación y el listado de mediadores donde conste el mediador suscriptor\n"
                                "4.- Generales de ley de la persona a quien se va a demandar\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "6.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 7 and genero == "F" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si" and alimentos == "No" and supa =="No"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificados de nacimiento de los hijos contemplados en el acta (vigente)\n"
                                "3.- Original o copia certificada del acta de mediación, acreditación del centro de mediación y el listado de mediadores donde conste el mediador suscriptor\n"
                                "4.- Generales de ley de la persona a quien se va a demandar\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "6.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 7 and genero == "M" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si" and alimentos == "No" and supa =="No"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificados de nacimiento de los hijos contemplados en el acta (vigente)\n"
                                "3.- Original o copia certificada del acta de mediación, acreditación del centro de mediación y el listado de mediadores donde conste el mediador suscriptor\n"
                                "4.- Generales de ley de la persona a quien se va a demandar\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "6.- Última declaraciónd e impuestos y sus tres últimos roles de pago\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 7 and genero == "F" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si" and alimentos == "No" and supa =="No"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificados de nacimiento de los hijos contemplados en el acta (vigente)\n"
                                "3.- Original o copia certificada del acta de mediación, acreditación del centro de mediación y el listado de mediadores donde conste el mediador suscriptor\n"
                                "4.- Generales de ley de la persona a quien se va a demandar\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "6.- Última declaraciónd e impuestos y sus tres últimos roles de pago\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 7 and genero == "M" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and alimentos == "No" and supa =="No"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificados de nacimiento de los hijos contemplados en el acta (vigente)\n"
                                "3.- Original o copia certificada del acta de mediación, acreditación del centro de mediación y el listado de mediadores donde conste el mediador suscriptor\n"
                                "4.- Generales de ley de la persona a quien se va a demandar\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "6.- Certificado de no afiliación al IESS\n" #Agregar nota de sacar captura de pantalla al estado de contribuyente en el SRI
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 7 and genero == "F" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and alimentos == "No" and supa =="No"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificados de nacimiento de los hijos contemplados en el acta (vigente)\n"
                                "3.- Original o copia certificada del acta de mediación, acreditación del centro de mediación y el listado de mediadores donde conste el mediador suscriptor\n"
                                "4.- Generales de ley de la persona a quien se va a demandar\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "6.- Certificado de no afiliación al IESS\n" #Agregar nota de sacar captura de pantalla al estado de contribuyente en el SRI
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 7 and genero == "M" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and alimentos == "No" and supa =="No"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificados de nacimiento de los hijos contemplados en el acta (vigente)\n"
                                "3.- Original o copia certificada del acta de mediación, acreditación del centro de mediación y el listado de mediadores donde conste el mediador suscriptor\n"
                                "4.- Generales de ley de la persona a quien se va a demandar\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "6.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 7 and genero == "F" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and alimentos == "No" and supa =="No"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificados de nacimiento de los hijos contemplados en el acta (vigente)\n"
                                "3.- Original o copia certificada del acta de mediación, acreditación del centro de mediación y el listado de mediadores donde conste el mediador suscriptor\n"
                                "4.- Generales de ley de la persona a quien se va a demandar\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "6.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")

                #Tenencia
                elif (int(caso[0]) == 8 and genero == "M" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado nacimiento original de todos sus hijos (vigente)\n"
                                "4.- Generales de ley de la persona a quien se va a demandar\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 8 and genero == "F" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado nacimiento original de todos sus hijos (vigente)\n"
                                "4.- Generales de ley de la persona a quien se va a demandar\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 8 and genero == "M" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Última declaración de impuestos y tres últimos roles de pago\n"
                                "3.- Certificado nacimiento original de todos sus hijos (vigente)\n"
                                "4.- Generales de ley de la persona a quien se va a demandar\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 8 and genero == "F" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Última declaración de impuestos y tres últimos roles de pago\n"
                                "3.- Certificado nacimiento original de todos sus hijos (vigente)\n"
                                "4.- Generales de ley de la persona a quien se va a demandar\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 8 and genero == "M" and iess == "No" and sri == "No" and estado_de_trabajo == "No"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de no afiliación al IESS\n" #Agregar nota
                                "3.- Certificado nacimiento original de todos sus hijos (vigente)\n"
                                "4.- Generales de ley de la persona a quien se va a demandar\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 8 and genero == "F" and iess == "No" and sri == "No" and estado_de_trabajo == "No"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de no afiliación al IESS\n" #Agregar nota
                                "3.- Certificado nacimiento original de todos sus hijos (vigente)\n"
                                "4.- Generales de ley de la persona a quien se va a demandar\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 8 and genero == "M" and iess == "No" and sri == "No" and estado_de_trabajo == "No"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de afiliación al IESS e historial de aportaciones\n" #Agregar nota
                                "3.- Certificado nacimiento original de todos sus hijos (vigente)\n"
                                "4.- Generales de ley de la persona a quien se va a demandar\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 8 and genero == "F" and iess == "No" and sri == "No" and estado_de_trabajo == "No"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de afiliación al IESS e historial de aportaciones\n" #Agregar nota
                                "3.- Certificado nacimiento original de todos sus hijos (vigente)\n"
                                "4.- Generales de ley de la persona a quien se va a demandar\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")

                #Privación, suspensión o limitación de la patria potestad causal ausencia  WIP REVISAR PUNTO 6
                elif (int(caso[0]) == 9 and genero == "M" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si" and ausencia == "Si"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado nacimiento original de todos sus hijos (vigente)\n"
                                "4.- Generales de ley de la persona a quien se va a demandar\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "6.-  \n"
                                "7.- copia certificada de la diligencia preparatoria de investigación policial y social.\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 9 and genero == "F" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si" and ausencia == "Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado nacimiento original de todos sus hijos (vigente)\n"
                                "4.- Generales de ley de la persona a quien se va a demandar\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "6.-  \n"
                                "7.- copia certificada de la diligencia preparatoria de investigación policial y social.\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 9 and genero == "M" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si" and ausencia == "Si"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Última declaración de impuestos y tres últimos roles de pago\n"
                                "3.- Certificado nacimiento original de todos sus hijos (vigente)\n"
                                "4.- Generales de ley de la persona a quien se va a demandar\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "6.-  \n"
                                "7.- copia certificada de la diligencia preparatoria de investigación policial y social.\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 9 and genero == "F" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si" and ausencia == "Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Última declaración de impuestos y tres últimos roles de pago\n"
                                "3.- Certificado nacimiento original de todos sus hijos (vigente)\n"
                                "4.- Generales de ley de la persona a quien se va a demandar\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "6.-  \n"
                                "7.- copia certificada de la diligencia preparatoria de investigación policial y social.\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 9 and genero == "M" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and ausencia == "Si"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de no afiliación al IESS\n" #Agregar nota
                                "3.- Certificado nacimiento original de todos sus hijos (vigente)\n"
                                "4.- Generales de ley de la persona a quien se va a demandar\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "6.-  \n"
                                "7.- copia certificada de la diligencia preparatoria de investigación policial y social.\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 9 and genero == "F" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and ausencia == "Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de no afiliación al IESS\n" #Agregar nota
                                "3.- Certificado nacimiento original de todos sus hijos (vigente)\n"
                                "4.- Generales de ley de la persona a quien se va a demandar\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "6.-  \n"
                                "7.- copia certificada de la diligencia preparatoria de investigación policial y social.\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 9 and genero == "M" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and ausencia == "Si"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de no afiliación al IESS, otros documentos que justifiquen ingresos en caso de haberloss\n" #Agregar nota
                                "3.- Certificado nacimiento original de todos sus hijos (vigente)\n"
                                "4.- Generales de ley de la persona a quien se va a demandar\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "6.-  \n"
                                "7.- copia certificada de la diligencia preparatoria de investigación policial y social.\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 9 and genero == "F" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and ausencia == "Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de no afiliación al IESS, otros documentos que justifiquen ingresos en caso de haberlos\n" #Agregar nota
                                "3.- Certificado nacimiento original de todos sus hijos (vigente)\n"
                                "4.- Generales de ley de la persona a quien se va a demandar\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "6.-  \n"
                                "7.- copia certificada de la diligencia preparatoria de investigación policial y social.\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                #Privación, suspensión o limitación de la patria potestad OTRA CAUSAL (Consultar Sierra esto es PLACEHOLDER)
                elif (int(caso[0]) == 9 and genero == "M" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si" and ausencia == "No"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado nacimiento original de todos sus hijos (vigente)\n"
                                "4.- Generales de ley de la persona a quien se va a demandar\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "6.-  \n"
                                "7.- copia certificada de la diligencia preparatoria de investigación policial y social.\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 9 and genero == "F" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si" and ausencia == "No"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado nacimiento original de todos sus hijos (vigente)\n"
                                "4.- Generales de ley de la persona a quien se va a demandar\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "6.-  \n"
                                "7.- copia certificada de la diligencia preparatoria de investigación policial y social.\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 9 and genero == "M" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si" and ausencia == "No"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Última declaración de impuestos y tres últimos roles de pago\n"
                                "3.- Certificado nacimiento original de todos sus hijos (vigente)\n"
                                "4.- Generales de ley de la persona a quien se va a demandar\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "6.-  \n"
                                "7.- copia certificada de la diligencia preparatoria de investigación policial y social.\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 9 and genero == "F" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si" and ausencia == "No"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Última declaración de impuestos y tres últimos roles de pago\n"
                                "3.- Certificado nacimiento original de todos sus hijos (vigente)\n"
                                "4.- Generales de ley de la persona a quien se va a demandar\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "6.-  \n"
                                "7.- copia certificada de la diligencia preparatoria de investigación policial y social.\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 9 and genero == "M" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and ausencia == "No"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de no afiliación al IESS\n" #Agregar nota
                                "3.- Certificado nacimiento original de todos sus hijos (vigente)\n"
                                "4.- Generales de ley de la persona a quien se va a demandar\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "6.-  \n"
                                "7.- copia certificada de la diligencia preparatoria de investigación policial y social.\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 9 and genero == "F" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and ausencia == "No"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de no afiliación al IESS\n" #Agregar nota
                                "3.- Certificado nacimiento original de todos sus hijos (vigente)\n"
                                "4.- Generales de ley de la persona a quien se va a demandar\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "6.-  \n"
                                "7.- copia certificada de la diligencia preparatoria de investigación policial y social.\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 9 and genero == "M" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and ausencia == "No"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de no afiliación al IESS, otros documentos que justifiquen ingresos en caso de haberloss\n" #Agregar nota
                                "3.- Certificado nacimiento original de todos sus hijos (vigente)\n"
                                "4.- Generales de ley de la persona a quien se va a demandar\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "6.-  \n"
                                "7.- copia certificada de la diligencia preparatoria de investigación policial y social.\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (int(caso[0]) == 9 and genero == "F" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and ausencia == "No"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de no afiliación al IESS, otros documentos que justifiquen ingresos en caso de haberlos\n" #Agregar nota
                                "3.- Certificado nacimiento original de todos sus hijos (vigente)\n"
                                "4.- Generales de ley de la persona a quien se va a demandar\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "6.-  \n"
                                "7.- copia certificada de la diligencia preparatoria de investigación policial y social.\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                
                #Medidas de Protección
                elif (caso == "10.- Medidas de protección" and genero == "M" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado nacimiento original de todos sus hijos (vigente)\n"
                                "4.- Certificados de nacimiento necesarios para acreditar parentesco\n"
                                "5.- Generales de la ley de la persona a la que se va a demandar (nombres completos, edad, dirección, estado civil, etc.)"
                                "6.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "10.- Medidas de protección" and genero == "F" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado nacimiento original de todos sus hijos (vigente)\n"
                                "4.- Certificados de nacimiento necesarios para acreditar parentesco\n"
                                "5.- Generales de la ley de la persona a la que se va a demandar (nombres completos, edad, dirección, estado civil, etc.)"
                                "6.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "10.- Medidas de protección" and genero == "M" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado nacimiento original de todos sus hijos (vigente)\n"
                                "4.- Certificados de nacimiento necesarios para acreditar parentesco\n"
                                "5.- Generales de la ley de la persona a la que se va a demandar (nombres completos, edad, dirección, estado civil, etc.)"
                                "6.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "10.- Medidas de protección" and genero == "F" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado nacimiento original de todos sus hijos (vigente)\n"
                                "4.- Certificados de nacimiento necesarios para acreditar parentesco\n"
                                "5.- Generales de la ley de la persona a la que se va a demandar (nombres completos, edad, dirección, estado civil, etc.)"
                                "6.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "10.- Medidas de protección" and genero == "M" and iess == "No" and sri == "No" and estado_de_trabajo == "No"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado nacimiento original de todos sus hijos (vigente)\n"
                                "4.- Certificados de nacimiento necesarios para acreditar parentesco\n"
                                "5.- Generales de la ley de la persona a la que se va a demandar (nombres completos, edad, dirección, estado civil, etc.)"
                                "6.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "10.- Medidas de protección" and genero == "F" and iess == "No" and sri == "No" and estado_de_trabajo == "No"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado nacimiento original de todos sus hijos (vigente)\n"
                                "4.- Certificados de nacimiento necesarios para acreditar parentesco\n"
                                "5.- Generales de la ley de la persona a la que se va a demandar (nombres completos, edad, dirección, estado civil, etc.)"
                                "6.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "10.- Medidas de protección" and genero == "M" and iess == "No" and sri == "No" and estado_de_trabajo == "No"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado nacimiento original de todos sus hijos (vigente)\n"
                                "4.- Certificados de nacimiento necesarios para acreditar parentesco\n"
                                "5.- Generales de la ley de la persona a la que se va a demandar (nombres completos, edad, dirección, estado civil, etc.)"
                                "6.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "10.- Medidas de protección" and genero == "F" and iess == "No" and sri == "No" and estado_de_trabajo == "No"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado nacimiento original de todos sus hijos (vigente)\n"
                                "4.- Certificados de nacimiento necesarios para acreditar parentesco\n"
                                "5.- Generales de la ley de la persona a la que se va a demandar (nombres completos, edad, dirección, estado civil, etc.)"
                                "6.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);\n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                
                #Impugnación de maternidad
                elif (caso == "11.- Impugnación de maternidad" and genero == "M" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado nacimiento original de todos sus hijos (vigente)\n"
                                "4.- Generales de la ley de la persona a la que se va a demandar (nombres completos, edad, dirección, estado civil, etc.)\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "11.- Impugnación de maternidad" and genero == "F" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado nacimiento original de todos sus hijos (vigente)\n"
                                "4.- Generales de la ley de la persona a la que se va a demandar (nombres completos, edad, dirección, estado civil, etc.)\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "11.- Impugnación de maternidad" and genero == "M" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado nacimiento original de todos sus hijos (vigente)\n"
                                "4.- Generales de la ley de la persona a la que se va a demandar (nombres completos, edad, dirección, estado civil, etc.)\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "11.- Impugnación de maternidad" and genero == "F" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado nacimiento original de todos sus hijos (vigente)\n"
                                "4.- Generales de la ley de la persona a la que se va a demandar (nombres completos, edad, dirección, estado civil, etc.)\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "11.- Impugnación de maternidad" and genero == "M" and iess == "No" and sri == "No" and estado_de_trabajo == "No"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado nacimiento original de todos sus hijos (vigente)\n"
                                "4.- Generales de la ley de la persona a la que se va a demandar (nombres completos, edad, dirección, estado civil, etc.)\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "11.- Impugnación de maternidad" and genero == "F" and iess == "No" and sri == "No" and estado_de_trabajo == "No"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado nacimiento original de todos sus hijos (vigente)\n"
                                "4.- Generales de la ley de la persona a la que se va a demandar (nombres completos, edad, dirección, estado civil, etc.)\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "11.- Impugnación de maternidad" and genero == "M" and iess == "No" and sri == "No" and estado_de_trabajo == "No"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado nacimiento original de todos sus hijos (vigente)\n"
                                "4.- Generales de la ley de la persona a la que se va a demandar (nombres completos, edad, dirección, estado civil, etc.)\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "11.- Impugnación de maternidad" and genero == "F" and iess == "No" and sri == "No" and estado_de_trabajo == "No"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado nacimiento original de todos sus hijos (vigente)\n"
                                "4.- Generales de la ley de la persona a la que se va a demandar (nombres completos, edad, dirección, estado civil, etc.)\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                
                #Impugnación de paternidad
                elif (caso == "12.- Impugnación de paternidad (No aplica en reconocimiento voluntario)" and genero == "M" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado nacimiento original (vigente)\n"
                                "4.- Partida íntegra de matrimonio (vigente)\n"
                                "5.- Generales de la ley de la persona a la que se va a demandar (nombres completos, edad, dirección, estado civil, etc.)\n"
                                "6.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "12.- Impugnación de paternidad (No aplica en reconocimiento voluntario)" and genero == "F" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado nacimiento original (vigente)\n"
                                "4.- Partida íntegra de matrimonio (vigente)\n"
                                "5.- Generales de la ley de la persona a la que se va a demandar (nombres completos, edad, dirección, estado civil, etc.)\n"
                                "6.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "12.- Impugnación de paternidad (No aplica en reconocimiento voluntario)" and genero == "M" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado nacimiento original (vigente)\n"
                                "4.- Partida íntegra de matrimonio (vigente)\n"
                                "5.- Generales de la ley de la persona a la que se va a demandar (nombres completos, edad, dirección, estado civil, etc.)\n"
                                "6.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "12.- Impugnación de paternidad (No aplica en reconocimiento voluntario)" and genero == "F" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado nacimiento original (vigente)\n"
                                "4.- Partida íntegra de matrimonio (vigente)\n"
                                "5.- Generales de la ley de la persona a la que se va a demandar (nombres completos, edad, dirección, estado civil, etc.)\n"
                                "6.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "12.- Impugnación de paternidad (No aplica en reconocimiento voluntario)" and genero == "M" and iess == "No" and sri == "No" and estado_de_trabajo == "No"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado nacimiento original (vigente)\n"
                                "4.- Partida íntegra de matrimonio (vigente)\n"
                                "5.- Generales de la ley de la persona a la que se va a demandar (nombres completos, edad, dirección, estado civil, etc.)\n"
                                "6.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "12.- Impugnación de paternidad (No aplica en reconocimiento voluntario)" and genero == "F" and iess == "No" and sri == "No" and estado_de_trabajo == "No"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado nacimiento original (vigente)\n"
                                "4.- Partida íntegra de matrimonio (vigente)\n"
                                "5.- Generales de la ley de la persona a la que se va a demandar (nombres completos, edad, dirección, estado civil, etc.)\n"
                                "6.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "12.- Impugnación de paternidad (No aplica en reconocimiento voluntario)" and genero == "M" and iess == "No" and sri == "No" and estado_de_trabajo == "No"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                            "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado nacimiento original (vigente)\n"
                                "4.- Partida íntegra de matrimonio (vigente)\n"
                                "5.- Generales de la ley de la persona a la que se va a demandar (nombres completos, edad, dirección, estado civil, etc.)\n"
                                "6.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "12.- Impugnación de paternidad (No aplica en reconocimiento voluntario)" and genero == "F" and iess == "No" and sri == "No" and estado_de_trabajo == "No"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado nacimiento original (vigente)\n"
                                "4.- Partida íntegra de matrimonio (vigente)\n"
                                "5.- Generales de la ley de la persona a la que se va a demandar (nombres completos, edad, dirección, estado civil, etc.)\n"
                                "6.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS);"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                
                #Divorcio por mutuo consentimiento sin hijos dependientes pero mayores
                elif (caso == "13.- Divorcio por mutuo consentimiento sin hijos dependientes" and genero == "M" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si" and mayor == "Si"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado de bienes inmuebles emitido por el Registro de la Propiedad de cada uno de los cónyuges"
                                "4.- Certificado nacimiento original de todos sus hijos mayores (vigente)\n"
                                "5.- Partida íntegra de matrimonio (vigente)\n"
                                "6.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                                "7.- Certificado de posesión vehicular emitido por la Agencia Nacional de Tránsito (ANT) de cada uno de los cónyuges (vigente);" #AQUI ME QUEDE
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "13.- Divorcio por mutuo consentimiento sin hijos dependientes" and genero == "F" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si" and mayor == "Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado de bienes inmuebles emitido por el Registro de la Propiedad de cada uno de los cónyuges"
                                "4.- Certificado nacimiento original de todos sus hijos mayores (vigente)\n"
                                "5.- Partida íntegra de matrimonio (vigente)\n"
                                "6.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                                "7.- Certificado de posesión vehicular emitido por la Agencia Nacional de Tránsito (ANT) de cada uno de los cónyuges (vigente);" #AQUI ME QUEDE
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "13.- Divorcio por mutuo consentimiento sin hijos dependientes" and genero == "M" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si" and mayor == "Si"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado de bienes inmuebles emitido por el Registro de la Propiedad de cada uno de los cónyuges"
                                "4.- Certificado nacimiento original de todos sus hijos mayores (vigente)\n"
                                "5.- Partida íntegra de matrimonio (vigente)\n"
                                "6.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                                "7.- Certificado de posesión vehicular emitido por la Agencia Nacional de Tránsito (ANT) de cada uno de los cónyuges (vigente);" #AQUI ME QUEDE
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "13.- Divorcio por mutuo consentimiento sin hijos dependientes" and genero == "F" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si" and mayor == "Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado de bienes inmuebles emitido por el Registro de la Propiedad de cada uno de los cónyuges"
                                "4.- Certificado nacimiento original de todos sus hijos mayores (vigente)\n"
                                "5.- Partida íntegra de matrimonio (vigente)\n"
                                "6.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                                "7.- Certificado de posesión vehicular emitido por la Agencia Nacional de Tránsito (ANT) de cada uno de los cónyuges (vigente);" #AQUI ME QUEDE
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "13.- Divorcio por mutuo consentimiento sin hijos dependientes" and genero == "M" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and mayor == "Si"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado de bienes inmuebles emitido por el Registro de la Propiedad de cada uno de los cónyuges"
                                "4.- Certificado nacimiento original de todos sus hijos mayores (vigente)\n"
                                "5.- Partida íntegra de matrimonio (vigente)\n"
                                "6.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                                "7.- Certificado de posesión vehicular emitido por la Agencia Nacional de Tránsito (ANT) de cada uno de los cónyuges (vigente);" #AQUI ME QUEDE
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "13.- Divorcio por mutuo consentimiento sin hijos dependientes" and genero == "F" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and mayor == "Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado de bienes inmuebles emitido por el Registro de la Propiedad de cada uno de los cónyuges"
                                "4.- Certificado nacimiento original de todos sus hijos mayores (vigente)\n"
                                "5.- Partida íntegra de matrimonio (vigente)\n"
                                "6.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                                "7.- Certificado de posesión vehicular emitido por la Agencia Nacional de Tránsito (ANT) de cada uno de los cónyuges (vigente);" #AQUI ME QUEDE
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "13.- Divorcio por mutuo consentimiento sin hijos dependientes" and genero == "M" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and mayor == "Si"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado de bienes inmuebles emitido por el Registro de la Propiedad de cada uno de los cónyuges"
                                "4.- Certificado nacimiento original de todos sus hijos mayores (vigente)\n"
                                "5.- Partida íntegra de matrimonio (vigente)\n"
                                "6.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                                "7.- Certificado de posesión vehicular emitido por la Agencia Nacional de Tránsito (ANT) de cada uno de los cónyuges (vigente);" #AQUI ME QUEDE
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "13.- Divorcio por mutuo consentimiento sin hijos dependientes" and genero == "F" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and mayor == "Si"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado de bienes inmuebles emitido por el Registro de la Propiedad de cada uno de los cónyuges"
                                "4.- Certificado nacimiento original de todos sus hijos mayores (vigente)\n"
                                "5.- Partida íntegra de matrimonio (vigente)\n"
                                "6.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                                "7.- Certificado de posesión vehicular emitido por la Agencia Nacional de Tránsito (ANT) de cada uno de los cónyuges (vigente);" #AQUI ME QUEDE
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                #Divorcio por mutuo consentimiento sin hijos
                elif (caso == "13.- Divorcio por mutuo consentimiento sin hijos dependientes" and genero == "M" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si" and mayor == "No"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado de bienes inmuebles emitido por el Registro de la Propiedad de cada uno de los cónyuges"
                                "4.- Partida íntegra de matrimonio (vigente)\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                                "6.- Certificado de posesión vehicular emitido por la Agencia Nacional de Tránsito (ANT) de cada uno de los cónyuges (vigente);" #AQUI ME QUEDE
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "13.- Divorcio por mutuo consentimiento sin hijos dependientes" and genero == "F" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si" and mayor == "No"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado de bienes inmuebles emitido por el Registro de la Propiedad de cada uno de los cónyuges"
                                "4.- Partida íntegra de matrimonio (vigente)\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                                "6.- Certificado de posesión vehicular emitido por la Agencia Nacional de Tránsito (ANT) de cada uno de los cónyuges (vigente);" #AQUI ME QUEDE
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "13.- Divorcio por mutuo consentimiento sin hijos dependientes" and genero == "M" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si" and mayor == "No"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado de bienes inmuebles emitido por el Registro de la Propiedad de cada uno de los cónyuges"
                                "4.- Partida íntegra de matrimonio (vigente)\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                                "6.- Certificado de posesión vehicular emitido por la Agencia Nacional de Tránsito (ANT) de cada uno de los cónyuges (vigente);" #AQUI ME QUEDE
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "13.- Divorcio por mutuo consentimiento sin hijos dependientes" and genero == "F" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si" and mayor == "No"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado de bienes inmuebles emitido por el Registro de la Propiedad de cada uno de los cónyuges"
                                "4.- Partida íntegra de matrimonio (vigente)\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                                "6.- Certificado de posesión vehicular emitido por la Agencia Nacional de Tránsito (ANT) de cada uno de los cónyuges (vigente);" #AQUI ME QUEDE
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "13.- Divorcio por mutuo consentimiento sin hijos dependientes" and genero == "M" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and mayor == "No"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado de bienes inmuebles emitido por el Registro de la Propiedad de cada uno de los cónyuges"
                                "4.- Partida íntegra de matrimonio (vigente)\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                                "6.- Certificado de posesión vehicular emitido por la Agencia Nacional de Tránsito (ANT) de cada uno de los cónyuges (vigente);" #AQUI ME QUEDE
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "13.- Divorcio por mutuo consentimiento sin hijos dependientes" and genero == "F" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and mayor == "No"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado de bienes inmuebles emitido por el Registro de la Propiedad de cada uno de los cónyuges"
                                "4.- Partida íntegra de matrimonio (vigente)\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                                "6.- Certificado de posesión vehicular emitido por la Agencia Nacional de Tránsito (ANT) de cada uno de los cónyuges (vigente);" #AQUI ME QUEDE
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "13.- Divorcio por mutuo consentimiento sin hijos dependientes" and genero == "M" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and mayor == "No"):
                    mensaje_familia = (f"Estimado usuario {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado de bienes inmuebles emitido por el Registro de la Propiedad de cada uno de los cónyuges"
                                "4.- Partida íntegra de matrimonio (vigente)\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                                "6.- Certificado de posesión vehicular emitido por la Agencia Nacional de Tránsito (ANT) de cada uno de los cónyuges (vigente);" #AQUI ME QUEDE
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "13.- Divorcio por mutuo consentimiento sin hijos dependientes" and genero == "F" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and mayor == "No"):
                    mensaje_familia = (f"Estimada usuaria {nombre_usuario}, le informamos que su causa ha sido aceptada a patrocinio por parte del Consultorio. Para ello necesitaremos que presente los siguiente documentos:\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado de bienes inmuebles emitido por el Registro de la Propiedad de cada uno de los cónyuges"
                                "4.- Partida íntegra de matrimonio (vigente)\n"
                                "5.- Croquis y dirección exacta del domicilio de la persona a la que se va a notificar, la que debe incluir: provincia, cantón, parroquia, barrio, calle principal, nomenclatura, y calle secundaria (de ser posible ubicación GPS)\n"
                                "6.- Certificado de posesión vehicular emitido por la Agencia Nacional de Tránsito (ANT) de cada uno de los cónyuges (vigente);" #AQUI ME QUEDE
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                
                #Divorcio por mutuo consentimiento con hijos dependientes donde se regulan alimentos
                elif (caso == "14.- Divorcio por mutuo consentimiento con hijos dependientes" and genero == "M" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si" and pension_divorcio == "Si"):
                    mensaje_familia = (f"Estimado solicitante {nombre_usuario}, le informamos que, tras la entrevista preliminar, su causa de divorcio por mutuo consentimeinto ha pasado a la siguiente etapa. Para continuar y obtener el patrocinio legal, necesitaremos la siguiente documentación\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado nacimiento original de todos sus hijos, sean o no del matrimonio (vigente)\n"
                                "4.- Partida íntegra de matrimonio (vigente)\n"
                                "5.- Dirección del último domicilio de los cónyuges;\n"
                                "6.- Copia certificada de la sentencia/auto de calificación.;\n"
                                "7.- Copia de cédula de la persona que va a ser el curador ad litem;\n"
                                "8.- 2 cartas de honorabilidad a favor del curador insinuado para el efecto y la copia de cédula de la persona que emite y firma la carta (original en esfero azul);\n"
                                "9.- Certificado de IESS y tres últimos roles de pago de la persona que será obligada; \n"
                                "10.- Certificado de bienes inmuebles del registro de la propiedad de cada uno de los cónyuges;    \n"
                                "11.- Certificado de poseer vehículos ANT de cada uno de los cónyuges.  \n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "14.- Divorcio por mutuo consentimiento con hijos dependientes" and genero == "F" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si" and pension_divorcio == "Si"):
                    mensaje_familia = (f"Estimado solicitante {nombre_usuario}, le informamos que, tras la entrevista preliminar, su causa de divorcio por mutuo consentimeinto ha pasado a la siguiente etapa. Para continuar y obtener el patrocinio legal, necesitaremos la siguiente documentación\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado nacimiento original de todos sus hijos, sean o no del matrimonio (vigente)\n"
                                "4.- Partida íntegra de matrimonio (vigente)\n"
                                "5.- Dirección del último domicilio de los cónyuges;\n"
                                "6.- Copia certificada de la sentencia/auto de calificación.;\n"
                                "7.- Copia de cédula de la persona que va a ser el curador ad litem;\n"
                                "8.- 2 cartas de honorabilidad a favor del curador insinuado para el efecto y la copia de cédula de la persona que emite y firma la carta (original en esfero azul);\n"
                                "9.- Certificado de IESS y tres últimos roles de pago de la persona que será obligada; \n"
                                "10.- Certificado de bienes inmuebles del registro de la propiedad de cada uno de los cónyuges;    \n"
                                "11.- Certificado de poseer vehículos ANT de cada uno de los cónyuges.  \n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "14.- Divorcio por mutuo consentimiento con hijos dependientes" and genero == "M" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si" and pension_divorcio == "Si"):
                    mensaje_familia = (f"Estimado solicitante {nombre_usuario}, le informamos que, tras la entrevista preliminar, su causa de divorcio por mutuo consentimeinto ha pasado a la siguiente etapa. Para continuar y obtener el patrocinio legal, necesitaremos la siguiente documentación\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Contribuyente emitido por el SRI, tres últimos roles de pao y última declaración de impuestos\n"
                                "3.- Certificado nacimiento original de todos sus hijos, sean o no del matrimonio (vigente)\n"
                                "4.- Partida íntegra de matrimonio (vigente)\n"
                                "5.- Dirección del último domicilio de los cónyuges;\n"
                                "6.- Copia certificada de la sentencia/auto de calificación.;\n"
                                "7.- Copia de cédula de la persona que va a ser el curador ad litem;\n"
                                "8.- 2 cartas de honorabilidad a favor del curador insinuado para el efecto y la copia de cédula de la persona que emite y firma la carta (original en esfero azul);\n"
                                "9.- Certificado de IESS y tres últimos roles de pago de la persona que será obligada; \n"
                                "10.- Certificado de bienes inmuebles del registro de la propiedad de cada uno de los cónyuges;    \n"
                                "11.- Certificado de poseer vehículos ANT de cada uno de los cónyuges.  \n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "14.- Divorcio por mutuo consentimiento con hijos dependientes" and genero == "F" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si" and pension_divorcio == "Si"):
                    mensaje_familia = (f"Estimada solicitante {nombre_usuario}, le informamos que, tras la entrevista preliminar, su causa de divorcio por mutuo consentimeinto ha pasado a la siguiente etapa. Para continuar y obtener el patrocinio legal, necesitaremos la siguiente documentación\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Contribuyente emitido por el SRI, tres últimos roles de pao y última declaración de impuestos\n"
                                "3.- Certificado nacimiento original de todos sus hijos, sean o no del matrimonio (vigente)\n"
                                "4.- Partida íntegra de matrimonio (vigente)\n"
                                "5.- Dirección del último domicilio de los cónyuges;\n"
                                "6.- Copia certificada de la sentencia/auto de calificación.;\n"
                                "7.- Copia de cédula de la persona que va a ser el curador ad litem;\n"
                                "8.- 2 cartas de honorabilidad a favor del curador insinuado para el efecto y la copia de cédula de la persona que emite y firma la carta (original en esfero azul);\n"
                                "9.- Certificado de IESS y tres últimos roles de pago de la persona que será obligada; \n"
                                "10.- Certificado de bienes inmuebles del registro de la propiedad de cada uno de los cónyuges;    \n"
                                "11.- Certificado de poseer vehículos ANT de cada uno de los cónyuges.  \n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "14.- Divorcio por mutuo consentimiento con hijos dependientes" and genero == "M" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and pension_divorcio == "Si"):
                    mensaje_familia = (f"Estimado solicitante {nombre_usuario}, le informamos que, tras la entrevista preliminar, su causa de divorcio por mutuo consentimeinto ha pasado a la siguiente etapa. Para continuar y obtener el patrocinio legal, necesitaremos la siguiente documentación\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de no afilicación al IESS, documentos que justifiquen ingresos en caso de tenerlos\n"
                                "3.- Certificado nacimiento original de todos sus hijos, sean o no del matrimonio (vigente)\n"
                                "4.- Partida íntegra de matrimonio (vigente)\n"
                                "5.- Dirección del último domicilio de los cónyuges;\n"
                                "6.- Copia certificada de la sentencia/auto de calificación.;\n"
                                "7.- Copia de cédula de la persona que va a ser el curador ad litem;\n"
                                "8.- 2 cartas de honorabilidad a favor del curador insinuado para el efecto y la copia de cédula de la persona que emite y firma la carta (original en esfero azul);\n"
                                "9.- Certificado de IESS y tres últimos roles de pago de la persona que será obligada; \n"
                                "10.- Certificado de bienes inmuebles del registro de la propiedad de cada uno de los cónyuges;    \n"
                                "11.- Certificado de poseer vehículos ANT de cada uno de los cónyuges.  \n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "14.- Divorcio por mutuo consentimiento con hijos dependientes" and genero == "F" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and pension_divorcio == "Si"):
                    mensaje_familia = (f"Estimado solicitante {nombre_usuario}, le informamos que, tras la entrevista preliminar, su causa de divorcio por mutuo consentimeinto ha pasado a la siguiente etapa. Para continuar y obtener el patrocinio legal, necesitaremos la siguiente documentación\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de no afilicación al IESS, documentos que justifiquen ingresos en caso de tenerlos\n"
                                "3.- Certificado nacimiento original de todos sus hijos, sean o no del matrimonio (vigente)\n"
                                "4.- Partida íntegra de matrimonio (vigente)\n"
                                "5.- Dirección del último domicilio de los cónyuges;\n"
                                "6.- Copia certificada de la sentencia/auto de calificación.;\n"
                                "7.- Copia de cédula de la persona que va a ser el curador ad litem;\n"
                                "8.- 2 cartas de honorabilidad a favor del curador insinuado para el efecto y la copia de cédula de la persona que emite y firma la carta (original en esfero azul);\n"
                                "9.- Certificado de IESS y tres últimos roles de pago de la persona que será obligada; \n"
                                "10.- Certificado de bienes inmuebles del registro de la propiedad de cada uno de los cónyuges;    \n"
                                "11.- Certificado de poseer vehículos ANT de cada uno de los cónyuges.  \n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "14.- Divorcio por mutuo consentimiento con hijos dependientes" and genero == "M" and iess == "Si" and sri == "No" and estado_de_trabajo == "No" and pension_divorcio == "Si"):
                    mensaje_familia = (f"Estimado solicitante {nombre_usuario}, le informamos que, tras la entrevista preliminar, su causa de divorcio por mutuo consentimeinto ha pasado a la siguiente etapa. Para continuar y obtener el patrocinio legal, necesitaremos la siguiente documentación\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de afilicación al IESS, documentos que justifiquen ingresos en caso de tenerlos\n"
                                "3.- Certificado nacimiento original de todos sus hijos, sean o no del matrimonio (vigente)\n"
                                "4.- Partida íntegra de matrimonio (vigente)\n"
                                "5.- Dirección del último domicilio de los cónyuges;\n"
                                "6.- Copia certificada de la sentencia/auto de calificación.;\n"
                                "7.- Copia de cédula de la persona que va a ser el curador ad litem;\n"
                                "8.- 2 cartas de honorabilidad a favor del curador insinuado para el efecto y la copia de cédula de la persona que emite y firma la carta (original en esfero azul);\n"
                                "9.- Certificado de IESS y tres últimos roles de pago de la persona que será obligada; \n"
                                "10.- Certificado de bienes inmuebles del registro de la propiedad de cada uno de los cónyuges;    \n"
                                "11.- Certificado de poseer vehículos ANT de cada uno de los cónyuges.  \n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "14.- Divorcio por mutuo consentimiento con hijos dependientes" and genero == "F" and iess == "si" and sri == "No" and estado_de_trabajo == "No" and pension_divorcio == "Si"):
                    mensaje_familia = (f"Estimada solicitante {nombre_usuario}, le informamos que, tras la entrevista preliminar, su causa de divorcio por mutuo consentimeinto ha pasado a la siguiente etapa. Para continuar y obtener el patrocinio legal, necesitaremos la siguiente documentación\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de afilicación al IESS, documentos que justifiquen ingresos en caso de tenerlos\n"
                                "3.- Certificado nacimiento original de todos sus hijos, sean o no del matrimonio (vigente)\n"
                                "4.- Partida íntegra de matrimonio (vigente)\n"
                                "5.- Dirección del último domicilio de los cónyuges;\n"
                                "6.- Copia certificada de la sentencia/auto de calificación.;\n"
                                "7.- Copia de cédula de la persona que va a ser el curador ad litem;\n"
                                "8.- 2 cartas de honorabilidad a favor del curador insinuado para el efecto y la copia de cédula de la persona que emite y firma la carta (original en esfero azul);\n"
                                "9.- Certificado de IESS y tres últimos roles de pago de la persona que será obligada; \n"
                                "10.- Certificado de bienes inmuebles del registro de la propiedad de cada uno de los cónyuges;    \n"
                                "11.- Certificado de poseer vehículos ANT de cada uno de los cónyuges.  \n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                #Divorcio por mutuo consentimiento con hijos dependientes no se regulan alimentos
                elif (caso == "14.- Divorcio por mutuo consentimiento con hijos dependientes" and genero == "M" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si" and pension_divorcio == "No"):
                    mensaje_familia = (f"Estimado solicitante {nombre_usuario}, le informamos que, tras la entrevista preliminar, su causa de divorcio por mutuo consentimeinto ha pasado a la siguiente etapa. Para continuar y obtener el patrocinio legal, necesitaremos la siguiente documentación\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado nacimiento original de todos sus hijos, sean o no del matrimonio (vigente)\n"
                                "4.- Partida íntegra de matrimonio (vigente)\n"
                                "5.- Dirección del último domicilio de los cónyuges;\n"
                                "6.- Copia certificada de la sentencia/auto de calificación.;\n"
                                "7.- Copia de cédula de la persona que va a ser el curador ad litem;\n"
                                "8.- 2 cartas de honorabilidad a favor del curador insinuado para el efecto y la copia de cédula de la persona que emite y firma la carta (original en esfero azul);\n"
                                "9.- Certificado de bienes inmuebles del registro de la propiedad de cada uno de los cónyuges;    \n"
                                "10.- Certificado de poseer vehículos ANT de cada uno de los cónyuges.  \n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "14.- Divorcio por mutuo consentimiento con hijos dependientes" and genero == "F" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si" and pension_divorcio == "No"):
                    mensaje_familia = (f"Estimado solicitante {nombre_usuario}, le informamos que, tras la entrevista preliminar, su causa de divorcio por mutuo consentimeinto ha pasado a la siguiente etapa. Para continuar y obtener el patrocinio legal, necesitaremos la siguiente documentación\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado nacimiento original de todos sus hijos, sean o no del matrimonio (vigente)\n"
                                "4.- Partida íntegra de matrimonio (vigente)\n"
                                "5.- Dirección del último domicilio de los cónyuges;\n"
                                "6.- Copia certificada de la sentencia/auto de calificación.;\n"
                                "7.- Copia de cédula de la persona que va a ser el curador ad litem;\n"
                                "8.- 2 cartas de honorabilidad a favor del curador insinuado para el efecto y la copia de cédula de la persona que emite y firma la carta (original en esfero azul);\n"
                                "9.- Certificado de bienes inmuebles del registro de la propiedad de cada uno de los cónyuges;    \n"
                                "10.- Certificado de poseer vehículos ANT de cada uno de los cónyuges.  \n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "14.- Divorcio por mutuo consentimiento con hijos dependientes" and genero == "M" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si" and pension_divorcio == "No"):
                    mensaje_familia = (f"Estimado solicitante {nombre_usuario}, le informamos que, tras la entrevista preliminar, su causa de divorcio por mutuo consentimeinto ha pasado a la siguiente etapa. Para continuar y obtener el patrocinio legal, necesitaremos la siguiente documentación\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Contribuyente emitido por el SRI, tres últimos roles de pao y última declaración de impuestos\n"
                                "3.- Certificado nacimiento original de todos sus hijos, sean o no del matrimonio (vigente)\n"
                                "4.- Partida íntegra de matrimonio (vigente)\n"
                                "5.- Dirección del último domicilio de los cónyuges;\n"
                                "6.- Copia certificada de la sentencia/auto de calificación.;\n"
                                "7.- Copia de cédula de la persona que va a ser el curador ad litem;\n"
                                "8.- 2 cartas de honorabilidad a favor del curador insinuado para el efecto y la copia de cédula de la persona que emite y firma la carta (original en esfero azul);\n"
                                "9.- Certificado de bienes inmuebles del registro de la propiedad de cada uno de los cónyuges;    \n"
                                "10.- Certificado de poseer vehículos ANT de cada uno de los cónyuges.  \n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "14.- Divorcio por mutuo consentimiento con hijos dependientes" and genero == "F" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si" and pension_divorcio == "No"):
                    mensaje_familia = (f"Estimada solicitante {nombre_usuario}, le informamos que, tras la entrevista preliminar, su causa de divorcio por mutuo consentimeinto ha pasado a la siguiente etapa. Para continuar y obtener el patrocinio legal, necesitaremos la siguiente documentación\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Contribuyente emitido por el SRI, tres últimos roles de pao y última declaración de impuestos\n"
                                "3.- Certificado nacimiento original de todos sus hijos, sean o no del matrimonio (vigente)\n"
                                "4.- Partida íntegra de matrimonio (vigente)\n"
                                "5.- Dirección del último domicilio de los cónyuges;\n"
                                "6.- Copia certificada de la sentencia/auto de calificación.;\n"
                                "7.- Copia de cédula de la persona que va a ser el curador ad litem;\n"
                                "8.- 2 cartas de honorabilidad a favor del curador insinuado para el efecto y la copia de cédula de la persona que emite y firma la carta (original en esfero azul);\n"
                                "9.- Certificado de bienes inmuebles del registro de la propiedad de cada uno de los cónyuges;    \n"
                                "10.- Certificado de poseer vehículos ANT de cada uno de los cónyuges.  \n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "14.- Divorcio por mutuo consentimiento con hijos dependientes" and genero == "M" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and pension_divorcio == "No"):
                    mensaje_familia = (f"Estimado solicitante {nombre_usuario}, le informamos que, tras la entrevista preliminar, su causa de divorcio por mutuo consentimeinto ha pasado a la siguiente etapa. Para continuar y obtener el patrocinio legal, necesitaremos la siguiente documentación\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de no afilicación al IESS, documentos que justifiquen ingresos en caso de tenerlos\n"
                                "3.- Certificado nacimiento original de todos sus hijos, sean o no del matrimonio (vigente)\n"
                                "4.- Partida íntegra de matrimonio (vigente)\n"
                                "5.- Dirección del último domicilio de los cónyuges;\n"
                                "6.- Copia certificada de la sentencia/auto de calificación.;\n"
                                "7.- Copia de cédula de la persona que va a ser el curador ad litem;\n"
                                "8.- 2 cartas de honorabilidad a favor del curador insinuado para el efecto y la copia de cédula de la persona que emite y firma la carta (original en esfero azul);\n"
                                "9.- Certificado de bienes inmuebles del registro de la propiedad de cada uno de los cónyuges;    \n"
                                "10.- Certificado de poseer vehículos ANT de cada uno de los cónyuges.  \n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "14.- Divorcio por mutuo consentimiento con hijos dependientes" and genero == "F" and iess == "No" and sri == "No" and estado_de_trabajo == "No" and pension_divorcio == "No"):
                    mensaje_familia = (f"Estimado solicitante {nombre_usuario}, le informamos que, tras la entrevista preliminar, su causa de divorcio por mutuo consentimeinto ha pasado a la siguiente etapa. Para continuar y obtener el patrocinio legal, necesitaremos la siguiente documentación\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de no afilicación al IESS, documentos que justifiquen ingresos en caso de tenerlos\n"
                                "3.- Certificado nacimiento original de todos sus hijos, sean o no del matrimonio (vigente)\n"
                                "4.- Partida íntegra de matrimonio (vigente)\n"
                                "5.- Dirección del último domicilio de los cónyuges;\n"
                                "6.- Copia certificada de la sentencia/auto de calificación.;\n"
                                "7.- Copia de cédula de la persona que va a ser el curador ad litem;\n"
                                "8.- 2 cartas de honorabilidad a favor del curador insinuado para el efecto y la copia de cédula de la persona que emite y firma la carta (original en esfero azul);\n"
                                "9.- Certificado de bienes inmuebles del registro de la propiedad de cada uno de los cónyuges;    \n"
                                "10.- Certificado de poseer vehículos ANT de cada uno de los cónyuges.  \n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "14.- Divorcio por mutuo consentimiento con hijos dependientes" and genero == "M" and iess == "Si" and sri == "No" and estado_de_trabajo == "No" and pension_divorcio == "No"):
                    mensaje_familia = (f"Estimado solicitante {nombre_usuario}, le informamos que, tras la entrevista preliminar, su causa de divorcio por mutuo consentimeinto ha pasado a la siguiente etapa. Para continuar y obtener el patrocinio legal, necesitaremos la siguiente documentación\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de afilicación al IESS, documentos que justifiquen ingresos en caso de tenerlos\n"
                                "3.- Certificado nacimiento original de todos sus hijos, sean o no del matrimonio (vigente)\n"
                                "4.- Partida íntegra de matrimonio (vigente)\n"
                                "5.- Dirección del último domicilio de los cónyuges;\n"
                                "6.- Copia certificada de la sentencia/auto de calificación.;\n"
                                "7.- Copia de cédula de la persona que va a ser el curador ad litem;\n"
                                "8.- 2 cartas de honorabilidad a favor del curador insinuado para el efecto y la copia de cédula de la persona que emite y firma la carta (original en esfero azul);\n"
                                "9.- Certificado de bienes inmuebles del registro de la propiedad de cada uno de los cónyuges;    \n"
                                "10.- Certificado de poseer vehículos ANT de cada uno de los cónyuges.  \n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "14.- Divorcio por mutuo consentimiento con hijos dependientes" and genero == "F" and iess == "Si" and sri == "No" and estado_de_trabajo == "No" and pension_divorcio == "No"):
                    mensaje_familia = (f"Estimada solicitante {nombre_usuario}, le informamos que, tras la entrevista preliminar, su causa de divorcio por mutuo consentimeinto ha pasado a la siguiente etapa. Para continuar y obtener el patrocinio legal, necesitaremos la siguiente documentación\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de afilicación al IESS, documentos que justifiquen ingresos en caso de tenerlos\n"
                                "3.- Certificado nacimiento original de todos sus hijos, sean o no del matrimonio (vigente)\n"
                                "4.- Partida íntegra de matrimonio (vigente)\n"
                                "5.- Dirección del último domicilio de los cónyuges;\n"
                                "6.- Copia certificada de la sentencia/auto de calificación.;\n"
                                "7.- Copia de cédula de la persona que va a ser el curador ad litem;\n"
                                "8.- 2 cartas de honorabilidad a favor del curador insinuado para el efecto y la copia de cédula de la persona que emite y firma la carta (original en esfero azul);\n"
                                "9.- Certificado de bienes inmuebles del registro de la propiedad de cada uno de los cónyuges;    \n"
                                "10.- Certificado de poseer vehículos ANT de cada uno de los cónyuges.  \n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                
                #Curaduria para nuupcias
                elif (caso == "15.- Curaduría para nupcias" and genero == "M" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si"):
                    mensaje_familia = (f"Estimado solicitante {nombre_usuario}, le informamos que, tras la entrevista preliminar, su causa de divorcio por mutuo consentimeinto ha pasado a la siguiente etapa. Para continuar y obtener el patrocinio legal, necesitaremos la siguiente documentación\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones;\n"
                                "3.- Certificado nacimiento original de de los hijos para quienes se realiza la curaduría (vigente);\n"
                                "4.- Generales de ley y copia de cédula de quien será el curador;\n"
                                "5.- Dos cartas de honorabilidad para el Curador insinuado;\n"
                                "6.- Copia de cédula de quien firma la carta de honorabilidad; \n"
                                "7.- Certificado del Registro de la propiedad a nombre de los hijos a quien se aplica la curaduría; y\n"
                                "8.- Certificado de poseer vehículo ANT de los hijos a quien se aplica curaduría. \n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "15.- Curaduría para nupcias" and genero == "F" and iess == "Si" and sri == "No" and estado_de_trabajo == "Si"):
                    mensaje_familia = (f"Estimada solicitante {nombre_usuario}, le informamos que, tras la entrevista preliminar, su causa de divorcio por mutuo consentimeinto ha pasado a la siguiente etapa. Para continuar y obtener el patrocinio legal, necesitaremos la siguiente documentación\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Afiliación al IESS e historial de aportaciones\n"
                                "3.- Certificado nacimiento original de de los hijos para quienes se realiza la curaduría (vigente);\n"
                                "4.- Generales de ley y copia de cédula de quien será el curador;\n"
                                "5.- Dos cartas de honorabilidad para el Curador insinuado;\n"
                                "6.- Copia de cédula de quien firma la carta de honorabilidad; \n"
                                "7.- Certificado del Registro de la propiedad a nombre de los hijos a quien se aplica la curaduría; y\n"
                                "8.- Certificado de poseer vehículo ANT de los hijos a quien se aplica curaduría. \n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "15.- Curaduría para nupcias" and genero == "M" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si"):
                    mensaje_familia = (f"Estimado solicitante {nombre_usuario}, le informamos que, tras la entrevista preliminar, su causa de divorcio por mutuo consentimeinto ha pasado a la siguiente etapa. Para continuar y obtener el patrocinio legal, necesitaremos la siguiente documentación\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Contribuyente emitido por el SRI, tres últimos roles de pao y última declaración de impuestos\n"
                                "3.- Certificado nacimiento original de de los hijos para quienes se realiza la curaduría (vigente);\n"
                                "4.- Generales de ley y copia de cédula de quien será el curador;\n"
                                "5.- Dos cartas de honorabilidad para el Curador insinuado;\n"
                                "6.- Copia de cédula de quien firma la carta de honorabilidad; \n"
                                "7.- Certificado del Registro de la propiedad a nombre de los hijos a quien se aplica la curaduría; y\n"
                                "8.- Certificado de poseer vehículo ANT de los hijos a quien se aplica curaduría. \n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "15.- Curaduría para nupcias" and genero == "F" and iess == "No" and sri == "Si" and estado_de_trabajo == "Si"):
                    mensaje_familia = (f"Estimada solicitante {nombre_usuario}, le informamos que, tras la entrevista preliminar, su causa de divorcio por mutuo consentimeinto ha pasado a la siguiente etapa. Para continuar y obtener el patrocinio legal, necesitaremos la siguiente documentación\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de Contribuyente emitido por el SRI, tres últimos roles de pao y última declaración de impuestos\n"
                                "3.- Certificado nacimiento original de de los hijos para quienes se realiza la curaduría (vigente);\n"
                                "4.- Generales de ley y copia de cédula de quien será el curador;\n"
                                "5.- Dos cartas de honorabilidad para el Curador insinuado;\n"
                                "6.- Copia de cédula de quien firma la carta de honorabilidad; \n"
                                "7.- Certificado del Registro de la propiedad a nombre de los hijos a quien se aplica la curaduría; y\n"
                                "8.- Certificado de poseer vehículo ANT de los hijos a quien se aplica curaduría. \n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "15.- Curaduría para nupcias" and genero == "M" and iess == "No" and sri == "No" and estado_de_trabajo == "No"):
                    mensaje_familia = (f"Estimado solicitante {nombre_usuario}, le informamos que, tras la entrevista preliminar, su causa de divorcio por mutuo consentimeinto ha pasado a la siguiente etapa. Para continuar y obtener el patrocinio legal, necesitaremos la siguiente documentación\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de no afilicación al IESS, documentos que justifiquen ingresos en caso de tenerlos\n"
                                "3.- Certificado nacimiento original de de los hijos para quienes se realiza la curaduría (vigente);\n"
                                "4.- Generales de ley y copia de cédula de quien será el curador;\n"
                                "5.- Dos cartas de honorabilidad para el Curador insinuado;\n"
                                "6.- Copia de cédula de quien firma la carta de honorabilidad; \n"
                                "7.- Certificado del Registro de la propiedad a nombre de los hijos a quien se aplica la curaduría; y\n"
                                "8.- Certificado de poseer vehículo ANT de los hijos a quien se aplica curaduría. \n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "15.- Curaduría para nupcias" and genero == "F" and iess == "No" and sri == "No" and estado_de_trabajo == "No"):
                    mensaje_familia = (f"Estimado solicitante {nombre_usuario}, le informamos que, tras la entrevista preliminar, su causa de divorcio por mutuo consentimeinto ha pasado a la siguiente etapa. Para continuar y obtener el patrocinio legal, necesitaremos la siguiente documentación\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de no afilicación al IESS, documentos que justifiquen ingresos en caso de tenerlos\n"
                                "3.- Certificado nacimiento original de de los hijos para quienes se realiza la curaduría (vigente);\n"
                                "4.- Generales de ley y copia de cédula de quien será el curador;\n"
                                "5.- Dos cartas de honorabilidad para el Curador insinuado;\n"
                                "6.- Copia de cédula de quien firma la carta de honorabilidad; \n"
                                "7.- Certificado del Registro de la propiedad a nombre de los hijos a quien se aplica la curaduría; y\n"
                                "8.- Certificado de poseer vehículo ANT de los hijos a quien se aplica curaduría. \n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "15.- Curaduría para nupcias" and genero == "M" and iess == "Si" and sri == "No" and estado_de_trabajo == "No"):
                    mensaje_familia = (f"Estimado solicitante {nombre_usuario}, le informamos que, tras la entrevista preliminar, su causa de divorcio por mutuo consentimeinto ha pasado a la siguiente etapa. Para continuar y obtener el patrocinio legal, necesitaremos la siguiente documentación\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de afilicación al IESS, documentos que justifiquen ingresos en caso de tenerlos\n"
                                "3.- Certificado nacimiento original de de los hijos para quienes se realiza la curaduría (vigente);\n"
                                "4.- Generales de ley y copia de cédula de quien será el curador;\n"
                                "5.- Dos cartas de honorabilidad para el Curador insinuado;\n"
                                "6.- Copia de cédula de quien firma la carta de honorabilidad; \n"
                                "7.- Certificado del Registro de la propiedad a nombre de los hijos a quien se aplica la curaduría; y\n"
                                "8.- Certificado de poseer vehículo ANT de los hijos a quien se aplica curaduría. \n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")
                elif (caso == "15.- Curaduría para nupcias" and genero == "F" and iess == "Si" and sri == "No" and estado_de_trabajo == "No"):
                    mensaje_familia = (f"Estimada solicitante {nombre_usuario}, le informamos que, tras la entrevista preliminar, su causa de divorcio por mutuo consentimeinto ha pasado a la siguiente etapa. Para continuar y obtener el patrocinio legal, necesitaremos la siguiente documentación\n"
                                "   \n"
                                "1.- Copia de cédula vigente\n"
                                "2.- Certificado de afilicación al IESS, documentos que justifiquen ingresos en caso de tenerlos\n"
                                "3.- Certificado nacimiento original de de los hijos para quienes se realiza la curaduría (vigente);\n"
                                "4.- Generales de ley y copia de cédula de quien será el curador;\n"
                                "5.- Dos cartas de honorabilidad para el Curador insinuado;\n"
                                "6.- Copia de cédula de quien firma la carta de honorabilidad; \n"
                                "7.- Certificado del Registro de la propiedad a nombre de los hijos a quien se aplica la curaduría; y\n"
                                "8.- Certificado de poseer vehículo ANT de los hijos a quien se aplica curaduría. \n"
                                "   \n"
                                "Le recordamos que esta documentación deberá ser entregada en un máximo de 30 días contados desde la fecha de la entrevista.\n"
                                "Adicionalmente le informamos que los documentos emitidos por el Registro Civil, SRI, entre otros, tienen un tiempo de caducidad\n"
                                "desde su emisión, por lo que le pedimos tener muy en cuenta esto en los documentos que tienen la indicación de (vigente).")             
                
                
                
                else:
                    mensaje_familia = "Parámetros no definidos o caso no soportado." 
                mensaje_text_familia.insert(tk.END, mensaje_familia)
            except ValueError:
                messagebox.showerror("Error", "Ingrese los datos correctamente.")
        # Ventana 
        ventana_caso_familia = tk.Toplevel()
        ventana_caso_familia.title(f"Generador de Mensaje - Caso {caso}")
        ventana_caso_familia.geometry("1080x1000")
        

        tk.Label(ventana_caso_familia, text="Nombre del Usuario").pack(pady=5)
        nombre_entry = tk.Entry(ventana_caso_familia)
        nombre_entry.pack(pady=5)

        tk.Label(ventana_caso_familia, text="Género (M/F)").pack(pady=5)
        genero_var = tk.StringVar(value="")
        tk.OptionMenu(ventana_caso_familia, genero_var, "M", "F").pack(pady=5)

        tk.Label(ventana_caso_familia, text="¿Tiene trabajo? (si/no)").pack(pady=5)
        trabajo_var = tk.StringVar(value="")
        tk.OptionMenu(ventana_caso_familia, trabajo_var, "Si", "No").pack(pady=5)

        tk.Label(ventana_caso_familia, text="¿Está afiliado al IESS? (si/no)").pack(pady=5)
        iess_var = tk.StringVar(value="")
        tk.OptionMenu(ventana_caso_familia, iess_var, "Si", "No").pack(pady=5)

        tk.Label(ventana_caso_familia, text="¿Posee RUC vigente? (si/no)").pack(pady=5)
        sri_var = tk.StringVar(value="")
        tk.OptionMenu(ventana_caso_familia, sri_var, "Si", "No").pack(pady=5)


        # Botones condicionales 
        if int(caso[0]) == 4:
            tk.Label(ventana_caso_familia, text="¿Nació el bebé? (si/no)").pack(pady=5)
            global bebe_var  
            bebe_var = tk.StringVar(value="")
            tk.OptionMenu(ventana_caso_familia, bebe_var, "Si", "No").pack(pady=5)
        elif int(caso[0]) == 5:
            tk.Label(ventana_caso_familia, text="¿Es la parte obligada? (si/no)").pack(pady=5)
            global obligado_var 
            obligado_var = tk.StringVar(value="")
            tk.OptionMenu(ventana_caso_familia, obligado_var, "Si", "No").pack(pady=5)
        elif int(caso[0]) == 2:
            tk.Label(ventana_caso_familia, text="¿Posee el titular del derecho alguna discapacidad? (si/no)").pack(pady=5)
            global discapacidad_var 
            discapacidad_var = tk.StringVar(value="")
            tk.OptionMenu(ventana_caso_familia, discapacidad_var, "Si", "No").pack(pady=5)
        elif int(caso[0]) == 3:
            tk.Label(ventana_caso_familia, text="¿Posee el titular del derecho alguna discapacidad? (si/no)").pack(pady=5)
            global discapacidad3_var 
            discapacidad3_var = tk.StringVar(value="")
            tk.OptionMenu(ventana_caso_familia, discapacidad3_var, "Si", "No").pack(pady=5) 
        elif int(caso[0]) == 6:
            tk.Label (ventana_caso_familia, text="¿Tiene pensiones pendientes devengadas? (Si/No)").pack(pady=5)
            global pension_var
            pension_var = tk.StringVar(value="")
            tk.OptionMenu(ventana_caso_familia, pension_var, "Si", "No").pack(pady=5)
        elif int(caso[0]) == 7:
            tk.Label (ventana_caso_familia, text="¿La ejecución de acta de mediación es en materia de alimentos? (Si/No)").pack(pady=5)
            global alimentos_var
            alimentos_var = tk.StringVar(value="")
            tk.OptionMenu(ventana_caso_familia, alimentos_var, "Si", "No").pack(pady=5)

            tk.Label (ventana_caso_familia, text="¿Se encuentra ya vinculada una cuenta SUPA? (En caso de cambiarla seleccionar No) (Si/No)").pack(pady=5)
            global supa_var
            supa_var = tk.StringVar(value="")
            tk.OptionMenu(ventana_caso_familia, supa_var, "Si", "No").pack(pady=5)
        elif int(caso[0]) == 9:
            tk.Label (ventana_caso_familia, text="¿Es causal Suspensión/privación o limitación con causal de ausencia? (Si/No)").pack(pady=5)
            global ausencia_var
            ausencia_var = tk.StringVar(value="")
            tk.OptionMenu(ventana_caso_familia, ausencia_var, "Si", "No").pack(pady=5)
        elif caso == "13.- Divorcio por mutuo consentimiento sin hijos dependientes":
            tk.Label (ventana_caso_familia, text="¿Tiene hijos mayores? (Si/No)").pack(pady=5)
            global mayor_var
            mayor_var = tk.StringVar(value="")
            tk.OptionMenu(ventana_caso_familia, mayor_var, "Si", "No").pack(pady=5)
        elif caso == "14.- Divorcio por mutuo consentimiento con hijos dependientes":
            tk.Label (ventana_caso_familia, text= "¿Se regulará la pensión alimenticia? (Si/No)").pack(pady=5)
            global pension_divorcio_var
            pension_divorcio_var = tk.StringVar(value="")
            tk.OptionMenu(ventana_caso_familia, pension_divorcio_var, "Si", "No").pack(pady=5)
        elif caso == "16.- Divorcio por causal sin hijos dependientes":
            tk.Label (ventana_caso_familia, text= "¿Tienen hijos? (Si/No)").pack(pady=5)
            global hijos_causal_var
            hijos_causal_var = tk.StringVar(value="")
            tk.OptionMenu(ventana_caso_familia, hijos_causal_var, "Si", "No").pack(pady=5) 
        elif caso == "17.- Divorcio por causal con hijos dependientes":
            tk.Label (ventana_caso_familia, text= "¿Existe un proceso respecto a los hijos? (Si/No)").pack(pady=5)
            global causal_proceso_var
            causal_proceso_var = tk.StringVar(value="")
            tk.OptionMenu(ventana_caso_familia, causal_proceso_var, "Si", "No").pack(pady=5)  
        # Botón para generar mensaje
        tk.Button(ventana_caso_familia, text="Generar Mensaje", command=generar_mensaje).pack(pady=10)
        #boton para regresar a la seleccion
        tk.Button(ventana_caso_familia, text="Regresar", command=lambda: regresar_seleccion_familia(ventana_caso_familia)).pack(padx=30)

        # Widget de texto para mostrar el mensaje generado
        tk.Label(ventana_caso_familia, text="Mensaje generado:").pack(pady=5)
        mensaje_text_familia = tk.Text(ventana_caso_familia, height=40, width=90)
        mensaje_text_familia.pack(pady=10)

    ventanaf = tk.Toplevel()
    ventanaf.title("Mensaje Anexo 2 Materia de Familia")
    ventanaf.geometry("700x700")
    tk.Label(ventanaf, text="Ventana de Anexo 2 - Materia de Familia").pack(pady=10)
    tk.Button(ventanaf, text="Regresar a Selección", command=lambda: regresar_a_seleccion(ventanaf)).pack(pady=20)

    tk.Label(ventanaf, text="Seleccione un caso").pack(pady=10)
    tk.Label(ventanaf, text="(Elige 2 opciones y prueba con todas las combinaciones que se te ocurran)").pack(pady=10)
    #menú de selección de casos
    caso_var = tk.StringVar(value="")
    casos_opciones = [
        "1.- Familia iniciado",
        "2.- Familia no iniciado",
        "3.- Pensión con presunción de paternidad",
        "4.- Pensión de alimentos de mujer embarazada",
        "5.- Proceso de cobro de deuda de pensiones art. 137 COGEP",
        "6.- Extinción de pensión alimenticia",
        "7.- Ejecución de acta de mediación FMNA",
        "8.- Tenencia o visitas no iniciado",
        "9.- Privación, suspensión o limitación de patria potestad",
        "10.- Medidas de protección",
        "11.- Impugnación de maternidad",
        "12.- Impugnación de paternidad (No aplica en reconocimiento voluntario)",
        "13.- Divorcio por mutuo consentimiento sin hijos dependientes",
        "14.- Divorcio por mutuo consentimiento con hijos dependientes",
        "15.- Curaduría para nupcias",
        "16.- Divorcio por causal sin hijos dependientes",
        "17.- Divorcio por causal con hijos dependientes"
        ]
    menu_casos = tk.OptionMenu(ventanaf, caso_var, *casos_opciones)
    menu_casos.pack(pady=20)
    tk.Button(ventanaf, text="Confirmar Caso", command=abrir_ventana_caso_familia).pack(pady=20)
    
def ventana_laboral():
    ventana = tk.Toplevel()
    ventana.title("Mensaje Anexo 2 Materia Laboral")
    tk.Label(ventana, text="Ventana de Anexo 2 - Materia Laboral").pack(pady=10)
    tk.Button(ventana, text="Regresar a Selección", command=lambda: regresar_a_seleccion(ventana)).pack(pady=20)

def ventana_penal():
    ventana = tk.Toplevel()
    ventana.title("Mensaje Anexo 2 Materia Penal")
    tk.Label(ventana, text="Ventana de Anexo 2 - Materia Penal").pack(pady=10)
    tk.Button(ventana, text="Regresar a Selección", command=lambda: regresar_a_seleccion(ventana)).pack(pady=20)

# Función para seleccionar y abrir la ventana según la opción seleccionada
def opcion_seleccionada():
    seleccion = funcion_var.get()
    ventana_seleccion.withdraw()  # Oculta la ventana de selección inicial
    if seleccion == "Mensaje inicial de WhatsApp":
        ventana_WhatsApp()
    elif seleccion == "Mensaje Anexo 2 Materia de Familia":
        ventana_familia()
    elif seleccion == "Mensaje Anexo 2 Materia Laboral":
        ventana_laboral()
    elif seleccion == "Mensaje Anexo 2 Materia Penal":
        ventana_penal()

# Fuventana de selección 
def mostrar_ventana_seleccion():
    global ventana_seleccion
    ventana_seleccion = tk.Tk()
    ventana_seleccion.title("Selección de función")
    ventana_seleccion.geometry("400x300")

    tk.Label(ventana_seleccion, text="Seleccione la función").pack(pady=10)

    global funcion_var
    funcion_var = tk.StringVar(value="")

    funcion_opciones = [
        "Mensaje inicial de WhatsApp",
        "Mensaje Anexo 2 Materia de Familia",
        "Mensaje Anexo 2 Materia Laboral",
        "Mensaje Anexo 2 Materia Penal"
    ]

   
    menu_funciones = tk.OptionMenu(ventana_seleccion, funcion_var, *funcion_opciones)
    menu_funciones.pack(pady=20)

    tk.Button(ventana_seleccion, text="Confirmar Función", command=opcion_seleccionada).pack(pady=20)

    ventana_seleccion.mainloop()


mostrar_ventana_seleccion()
