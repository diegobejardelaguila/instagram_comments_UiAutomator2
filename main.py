
import uiautomator2 as u2
import time

d = ""
try:
    d = u2.connect() # connect to device
    print(d.info) #verificar conexion 
    print(d.app_list_running()) #ver aplicaciones iniciadas

    #Abrimos instagram
    d.app_start("com.instagram.android", use_monkey=True)

    #Busqueda de publicacion mediante url
    def charge_url():
        time.sleep(2)
        url_publish = input("Ingresa url: ")
        d.open_url(url_publish.strip()) # limpiar url
        time.sleep(3)
        
    charge_url()    

    #abrir componente de comentarios de publicaciones
    while True:
        open_comments_publish = d(resourceId='com.instagram.android:id/row_feed_button_comment', className="android.widget.ImageView")
        if open_comments_publish.exists:
            time.sleep(2)
            open_comments_publish.click()
            break
        else:
            print("Publicacion no autorizada")
            charge_url()
            
            
    #Dirigite a la vista de la publicacion para asignar variables a los componentes
    #tenemos que validar todavia si se encuentra el componente para recien ahi activar el bucle
    time.sleep(2)
    comment = d(className='android.widget.EditText', resourceId='com.instagram.android:id/layout_comment_thread_edittext')
    publish_comment = d(className='android.widget.Button',  resourceId='com.instagram.android:id/layout_comment_thread_post_button_click_area')



    #Bucle para comentar la publicacion cada 10 segundos

    count = 0
    while True:
        comment.set_text("Esta es la mejor foto que vi en la semana")
        time.sleep(1)
        publish_comment.click()
        time.sleep(10)
        count += 1
        if count==3:
            print("terminamos")
            break

except:
    print("No existe conexion activa, intenta configurar y conectar tu equipo correctamente")

input()
