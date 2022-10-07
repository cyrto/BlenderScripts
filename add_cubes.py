import bpy



def generate():

    for x in range(10):
        for y in range(10):
            for z in range(10):
                location = (x,y,z)
                bpy.ops.mesh.primitive_cube_add(size=0.5, enter_editmode=False, align='WORLD', location=location, scale=(1, 1, 1))



def clear():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False, confirm=False)


def main():
    clear()
    generate()


if __name__ == "__main__":
    main()