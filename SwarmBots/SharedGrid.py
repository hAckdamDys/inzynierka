from BuildingGrid import BuildingGrid

class SharedGrid(BuildingGrid):
    def __init__(self, *args, **kwargs) -> None:
        # self.first_arg = kwargs.pop('first_arg')
        print(args)
        super().__init__(*args,**kwargs)

