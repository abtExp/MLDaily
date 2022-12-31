# write code to generate a new template with sections that can be filled

def create_update(utype='daily'):
    template = open(f'./templates/{utype}.md', 'r')
    
    