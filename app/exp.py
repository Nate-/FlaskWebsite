class Exp(object):
    def __init__(self, logo, name, pos, desc):
        """
        Stores input for use with resume.

        :type logo: str (logo filename)
        :type name: str (company name)
        :type pos: str (position at company)
        :type desc: str (description of work at company) 
        """
        self.logo = logo
        self.company = name
        self.position = pos
        self.desc = desc


