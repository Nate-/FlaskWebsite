class Project(object):
    def __init__(self, projName, projLink, projDesc, projTags):
        """
        Stores input for use with project template

        :type projName: str
        :type projLink: str
        :type projDesc: str
        :type projTags: List[str] (techs used to build project) 
        """
        self.name = projName
        self.link = projLink
        self.desc = projDesc
        self.tags = projTags