import os

def initsetup():

    try:
        cmd = 'django-admin startproject www .'
        print('creating a server .............')
        os.system(cmd)
        print('please wait...')

    except:
        print('error')

    else:
        createfile = 'VirtualHost.py'
        get_content = "virtual_hosts = {" \
                      "\n   'test.com:8000': 'root.urls'," \
                      "\n   'example.com:8000': 'ex.urls'," \
                      "\n}"


        print('we are creating files...')
        f = open(createfile, "w")
        print(f)
        f.write(get_content)
        f.close()

        word = 'INSTALLED_APPS'
        middletext = 'MIDDLEWARE = ['
        hostallow = 'ALLOWED_HOSTS = []'

        with open('www/settings.py', 'r') as fp:
            # read all lines in a list
            lines = fp.readlines()
            count = 0
            f = open('www/settings.py', 'w')

            for line in lines:
                # check if string present on a current line
                if line.find(word) != -1:
                    count += 1
                    print('Installing Module in to', word)
                    x = lines.index(line) + count
                    print('Finding the Line Number:', x)
                    print('Inserting bigsansar module in to', line)

                    code = "    'bigsansar.apps.BigsansarConfig'," \
                           "\n"

                    lines.insert(x, code)

                elif line.find(middletext) != -1:

                    print('Reading the lines', middletext)
                    xy = lines.index(line) + 1
                    print('Finding the Line Number:', xy)
                    print('Inserting bigsansar virtualhost middleware  in to', line)

                    middlecode = "    'bigsansar.core.host.VirtualHostMiddleware'," \
                                 "\n"
                    lines.insert(xy, middlecode)

                elif line.find(hostallow) != -1:
                    xyz = lines.index(line)

                    # delete lines
                    del lines[xyz]

                    hostcode = "ALLOWED_HOSTS = ['*']" \
                               "\n"
                    lines.insert(xyz, hostcode)

            contents = "".join(lines)
            f.write(contents)
            f.close()

    finally:

        print('Finished')
