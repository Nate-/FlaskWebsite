class Exp(object):
    def __init__(self, logo, name, pos, desc, tech):
        """
        Stores input for use with resume template

        :type logo: str (logo filename)
        :type name: str (company name)
        :type pos: str (position at company)
        :type desc: List[str] (paragraph description of work at company) 
        :type tech: List[str] (techs used at company)
        """
        self.logo = logo
        self.company = name
        self.position = pos
        self.desc = desc
        self.techs = tech


