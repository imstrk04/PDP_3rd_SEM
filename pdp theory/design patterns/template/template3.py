from abc import ABC, abstractmethod

# Template Method Pattern

class WebPageTemplate(ABC):
    def create_page(self):
        self.set_header()
        self.set_body()
        self.set_footer()

    @abstractmethod
    def set_header(self):
        pass

    @abstractmethod
    def set_body(self):
        pass

    @abstractmethod
    def set_footer(self):
        pass

# Concrete Templates

class HomePage(WebPageTemplate):
    def set_header(self):
        print("Home Page Header")

    def set_body(self):
        print("Welcome to our website!")

    def set_footer(self):
        print("Home Page Footer")

class AboutPage(WebPageTemplate):
    def set_header(self):
        print("About Us Header")

    def set_body(self):
        print("Learn more about our company.")

    def set_footer(self):
        print("About Us Footer")

class ContactPage(WebPageTemplate):
    def set_header(self):
        print("Contact Us Header")

    def set_body(self):
        print("Reach out to us for any inquiries.")

    def set_footer(self):
        print("Contact Us Footer")

# Client Code

home_page = HomePage()
about_page = AboutPage()
contact_page = ContactPage()

home_page.create_page()
print("\n" + "="*20 + "\n")
about_page.create_page()
print("\n" + "="*20 + "\n")
contact_page.create_page()
