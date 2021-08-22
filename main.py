from instapy import InstaPy

if __name__ == '__main__':
    # Inicio de sesion en instagram
    session = InstaPy(username="<usuario>", password="<contraseña>", headless_browser=False)
    # Modo sin navegador para un servicio -> headless_browser=True
    session.login()

    # Dar likes a algunas publicaciones con el # de gatos o cats
    session.like_by_tags(["cats", "gatos"], amount=10)
    # Evitamos dar like a post inapropiados con palabras claves
    session.set_dont_like(["naked", "nsfw"])
    # Seguimos a algunos de los que damos likes
    session.set_do_follow(True, percentage=50)

    # Especificamos que pueda dejar mensajes
    session.set_do_comment(True, percentage=50)
    # Especificamos los comentarios que puede dejar
    session.set_comments(["Nice!", "Sweet!", "Beautiful :heart_eyes:"])

    # Solo nos fijamos en usuarios con el numero de seguidores que queramos
    session.set_relationship_bounds(enabled=True, max_followers=10000)

    # Cerramos la sesion
    session.end()