```python
!git clone https://github.com/hukkelas/DeepPrivacy
! cd DeepPrivacy
```

    Cloning into 'DeepPrivacy'...
    remote: Enumerating objects: 37, done.[K
    remote: Counting objects: 100% (37/37), done.[K
    remote: Compressing objects: 100% (29/29), done.[K
    remote: Total 1426 (delta 16), reused 19 (delta 8), pack-reused 1389[K
    Receiving objects: 100% (1426/1426), 12.50 MiB | 7.46 MiB/s, done.
    Resolving deltas: 100% (931/931), done.
    


```python
!wget -c https://repo.continuum.io/archive/Anaconda3-5.1.0-Linux-x86_64.sh
!chmod +x Anaconda3-5.1.0-Linux-x86_64.sh
!bash ./Anaconda3-5.1.0-Linux-x86_64.sh -b -f -p /usr/local
!conda install pytorch torchvision cudatoolkit=10.0 -c pytorch -y
!conda install cython numpy scikit-learn>=0.2 matplotlib pandas tqdm tflib autopep8 moviepy opencv-python requests -y 
import sys
sys.path.append('/usr/local/lib/python3.6/site-packages/')

```

    --2020-08-19 06:16:21--  https://repo.continuum.io/archive/Anaconda3-5.1.0-Linux-x86_64.sh
    Resolving repo.continuum.io (repo.continuum.io)... 104.18.201.79, 104.18.200.79, 2606:4700::6812:c84f, ...
    Connecting to repo.continuum.io (repo.continuum.io)|104.18.201.79|:443... connected.
    HTTP request sent, awaiting response... 301 Moved Permanently
    Location: https://repo.anaconda.com/archive/Anaconda3-5.1.0-Linux-x86_64.sh [following]
    --2020-08-19 06:16:21--  https://repo.anaconda.com/archive/Anaconda3-5.1.0-Linux-x86_64.sh
    Resolving repo.anaconda.com (repo.anaconda.com)... 104.16.130.3, 104.16.131.3, 2606:4700::6810:8303, ...
    Connecting to repo.anaconda.com (repo.anaconda.com)|104.16.130.3|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 577996269 (551M) [application/x-sh]
    Saving to: ‘Anaconda3-5.1.0-Linux-x86_64.sh’
    
    Anaconda3-5.1.0-Lin 100%[===================>] 551.22M   235MB/s    in 2.3s    
    
    2020-08-19 06:16:24 (235 MB/s) - ‘Anaconda3-5.1.0-Linux-x86_64.sh’ saved [577996269/577996269]
    
    PREFIX=/usr/local
    installing: python-3.6.4-hc3d631a_1 ...
    Python 3.6.4 :: Anaconda, Inc.
    installing: ca-certificates-2017.08.26-h1d4fec5_0 ...
    installing: conda-env-2.6.0-h36134e3_1 ...
    installing: intel-openmp-2018.0.0-hc7b2577_8 ...
    installing: libgcc-ng-7.2.0-h7cc24e2_2 ...
    installing: libgfortran-ng-7.2.0-h9f7466a_2 ...
    installing: libstdcxx-ng-7.2.0-h7a57d05_2 ...
    installing: bzip2-1.0.6-h9a117a8_4 ...
    installing: expat-2.2.5-he0dffb1_0 ...
    installing: gmp-6.1.2-h6c8ec71_1 ...
    installing: graphite2-1.3.10-hf63cedd_1 ...
    installing: icu-58.2-h9c2bf20_1 ...
    installing: jbig-2.1-hdba287a_0 ...
    installing: jpeg-9b-h024ee3a_2 ...
    installing: libffi-3.2.1-hd88cf55_4 ...
    installing: libsodium-1.0.15-hf101ebd_0 ...
    installing: libtool-2.4.6-h544aabb_3 ...
    installing: libxcb-1.12-hcd93eb1_4 ...
    installing: lzo-2.10-h49e0be7_2 ...
    installing: mkl-2018.0.1-h19d6760_4 ...
    installing: ncurses-6.0-h9df7e31_2 ...
    installing: openssl-1.0.2n-hb7f436b_0 ...
    installing: patchelf-0.9-hf79760b_2 ...
    installing: pcre-8.41-hc27e229_1 ...
    installing: pixman-0.34.0-hceecf20_3 ...
    installing: tk-8.6.7-hc745277_3 ...
    installing: unixodbc-2.3.4-hc36303a_1 ...
    installing: xz-5.2.3-h55aa19d_2 ...
    installing: yaml-0.1.7-had09818_2 ...
    installing: zlib-1.2.11-ha838bed_2 ...
    installing: glib-2.53.6-h5d9569c_2 ...
    installing: hdf5-1.10.1-h9caa474_1 ...
    installing: libedit-3.1-heed3624_0 ...
    installing: libpng-1.6.34-hb9fc6fc_0 ...
    installing: libssh2-1.8.0-h9cfc8f7_4 ...
    installing: libtiff-4.0.9-h28f6b97_0 ...
    installing: libxml2-2.9.7-h26e45fe_0 ...
    installing: mpfr-3.1.5-h11a74b3_2 ...
    installing: pandoc-1.19.2.1-hea2e7c5_1 ...
    installing: readline-7.0-ha6073c6_4 ...
    installing: zeromq-4.2.2-hbedb6e5_2 ...
    installing: dbus-1.12.2-hc3f9b76_1 ...
    installing: freetype-2.8-hab7d2ae_1 ...
    installing: gstreamer-1.12.4-hb53b477_0 ...
    installing: libcurl-7.58.0-h1ad7b7a_0 ...
    installing: libxslt-1.1.32-h1312cb7_0 ...
    installing: mpc-1.0.3-hec55b23_5 ...
    installing: sqlite-3.22.0-h1bed415_0 ...
    installing: curl-7.58.0-h84994c4_0 ...
    installing: fontconfig-2.12.4-h88586e7_1 ...
    installing: gst-plugins-base-1.12.4-h33fb286_0 ...
    installing: alabaster-0.7.10-py36h306e16b_0 ...
    installing: asn1crypto-0.24.0-py36_0 ...
    installing: attrs-17.4.0-py36_0 ...
    installing: backports-1.0-py36hfa02d7e_1 ...
    installing: beautifulsoup4-4.6.0-py36h49b8c8c_1 ...
    installing: bitarray-0.8.1-py36h14c3975_1 ...
    installing: boto-2.48.0-py36h6e4cd66_1 ...
    installing: cairo-1.14.12-h77bcde2_0 ...
    installing: certifi-2018.1.18-py36_0 ...
    installing: chardet-3.0.4-py36h0f667ec_1 ...
    installing: click-6.7-py36h5253387_0 ...
    installing: cloudpickle-0.5.2-py36_1 ...
    installing: colorama-0.3.9-py36h489cec4_0 ...
    installing: contextlib2-0.5.5-py36h6c84a62_0 ...
    installing: dask-core-0.16.1-py36_0 ...
    installing: decorator-4.2.1-py36_0 ...
    installing: docutils-0.14-py36hb0f60f5_0 ...
    installing: entrypoints-0.2.3-py36h1aec115_2 ...
    installing: et_xmlfile-1.0.1-py36hd6bccc3_0 ...
    installing: fastcache-1.0.2-py36h14c3975_2 ...
    installing: filelock-2.0.13-py36h646ffb5_0 ...
    installing: glob2-0.6-py36he249c77_0 ...
    installing: gmpy2-2.0.8-py36hc8893dd_2 ...
    installing: greenlet-0.4.12-py36h2d503a6_0 ...
    installing: heapdict-1.0.0-py36_2 ...
    installing: idna-2.6-py36h82fb2a8_1 ...
    installing: imagesize-0.7.1-py36h52d8127_0 ...
    installing: ipython_genutils-0.2.0-py36hb52b0d5_0 ...
    installing: itsdangerous-0.24-py36h93cc618_1 ...
    installing: jdcal-1.3-py36h4c697fb_0 ...
    installing: lazy-object-proxy-1.3.1-py36h10fcdad_0 ...
    installing: llvmlite-0.21.0-py36ha241eea_0 ...
    installing: locket-0.2.0-py36h787c0ad_1 ...
    installing: lxml-4.1.1-py36hf71bdeb_1 ...
    installing: markupsafe-1.0-py36hd9260cd_1 ...
    installing: mccabe-0.6.1-py36h5ad9710_1 ...
    installing: mistune-0.8.3-py36_0 ...
    installing: mkl-service-1.1.2-py36h17a0993_4 ...
    installing: mpmath-1.0.0-py36hfeacd6b_2 ...
    installing: msgpack-python-0.5.1-py36h6bb024c_0 ...
    installing: multipledispatch-0.4.9-py36h41da3fb_0 ...
    installing: numpy-1.14.0-py36h3dfced4_1 ...
    installing: olefile-0.45.1-py36_0 ...
    installing: pandocfilters-1.4.2-py36ha6701b7_1 ...
    installing: parso-0.1.1-py36h35f843b_0 ...
    installing: path.py-10.5-py36h55ceabb_0 ...
    installing: pep8-1.7.1-py36_0 ...
    installing: pickleshare-0.7.4-py36h63277f8_0 ...
    installing: pkginfo-1.4.1-py36h215d178_1 ...
    installing: pluggy-0.6.0-py36hb689045_0 ...
    installing: ply-3.10-py36hed35086_0 ...
    installing: psutil-5.4.3-py36h14c3975_0 ...
    installing: ptyprocess-0.5.2-py36h69acd42_0 ...
    installing: py-1.5.2-py36h29bf505_0 ...
    installing: pycodestyle-2.3.1-py36hf609f19_0 ...
    installing: pycosat-0.6.3-py36h0a5515d_0 ...
    installing: pycparser-2.18-py36hf9f622e_1 ...
    installing: pycrypto-2.6.1-py36h14c3975_7 ...
    installing: pycurl-7.43.0.1-py36hb7f436b_0 ...
    installing: pyodbc-4.0.22-py36hf484d3e_0 ...
    installing: pyparsing-2.2.0-py36hee85983_1 ...
    installing: pysocks-1.6.7-py36hd97a5b1_1 ...
    installing: pytz-2017.3-py36h63b9c63_0 ...
    installing: pyyaml-3.12-py36hafb9ca4_1 ...
    installing: pyzmq-16.0.3-py36he2533c7_0 ...
    installing: qt-5.6.2-h974d657_12 ...
    installing: qtpy-1.3.1-py36h3691cc8_0 ...
    installing: rope-0.10.7-py36h147e2ec_0 ...
    installing: ruamel_yaml-0.15.35-py36h14c3975_1 ...
    installing: send2trash-1.4.2-py36_0 ...
    installing: simplegeneric-0.8.1-py36_2 ...
    installing: sip-4.18.1-py36h51ed4ed_2 ...
    installing: six-1.11.0-py36h372c433_1 ...
    installing: snowballstemmer-1.2.1-py36h6febd40_0 ...
    installing: sortedcontainers-1.5.9-py36_0 ...
    installing: sphinxcontrib-1.0-py36h6d0f590_1 ...
    installing: sqlalchemy-1.2.1-py36h14c3975_0 ...
    installing: tblib-1.3.2-py36h34cf8b6_0 ...
    installing: testpath-0.3.1-py36h8cadb63_0 ...
    installing: toolz-0.9.0-py36_0 ...
    installing: tornado-4.5.3-py36_0 ...
    installing: typing-3.6.2-py36h7da032a_0 ...
    installing: unicodecsv-0.14.1-py36ha668878_0 ...
    installing: wcwidth-0.1.7-py36hdf4376a_0 ...
    installing: webencodings-0.5.1-py36h800622e_1 ...
    installing: werkzeug-0.14.1-py36_0 ...
    installing: wrapt-1.10.11-py36h28b7045_0 ...
    installing: xlrd-1.1.0-py36h1db9f0c_1 ...
    installing: xlsxwriter-1.0.2-py36h3de1aca_0 ...
    installing: xlwt-1.3.0-py36h7b00a1f_0 ...
    installing: babel-2.5.3-py36_0 ...
    installing: backports.shutil_get_terminal_size-1.0.0-py36hfea85ff_2 ...
    installing: bottleneck-1.2.1-py36haac1ea0_0 ...
    installing: cffi-1.11.4-py36h9745a5d_0 ...
    installing: conda-verify-2.0.0-py36h98955d8_0 ...
    installing: cycler-0.10.0-py36h93f1223_0 ...
    installing: cytoolz-0.9.0-py36h14c3975_0 ...
    installing: h5py-2.7.1-py36h3585f63_0 ...
    installing: harfbuzz-1.7.4-hc5b324e_0 ...
    installing: html5lib-1.0.1-py36h2f9c1c0_0 ...
    installing: jedi-0.11.1-py36_0 ...
    installing: networkx-2.1-py36_0 ...
    installing: nltk-3.2.5-py36h7532b22_0 ...
    installing: numba-0.36.2-np114py36hc6662d5_0 ...
    installing: numexpr-2.6.4-py36hc4a3f9a_0 ...
    installing: openpyxl-2.4.10-py36_0 ...
    installing: packaging-16.8-py36ha668100_1 ...
    installing: partd-0.3.8-py36h36fd896_0 ...
    installing: pathlib2-2.3.0-py36h49efa8e_0 ...
    installing: pexpect-4.3.1-py36_0 ...
    installing: pillow-5.0.0-py36h3deb7b8_0 ...
    installing: pyqt-5.6.0-py36h0386399_5 ...
    installing: python-dateutil-2.6.1-py36h88d3b88_1 ...
    installing: pywavelets-0.5.2-py36he602eb0_0 ...
    installing: qtawesome-0.4.4-py36h609ed8c_0 ...
    installing: scipy-1.0.0-py36hbf646e7_0 ...
    installing: setuptools-38.4.0-py36_0 ...
    installing: singledispatch-3.4.0.3-py36h7a266c3_0 ...
    installing: sortedcollections-0.5.3-py36h3c761f9_0 ...
    installing: sphinxcontrib-websupport-1.0.1-py36hb5cb234_1 ...
    installing: sympy-1.1.1-py36hc6d1c1c_0 ...
    installing: terminado-0.8.1-py36_1 ...
    installing: traitlets-4.3.2-py36h674d592_0 ...
    installing: zict-0.1.3-py36h3a3bf81_0 ...
    installing: astroid-1.6.1-py36_0 ...
    installing: bleach-2.1.2-py36_0 ...
    installing: clyent-1.2.2-py36h7e57e65_1 ...
    installing: cryptography-2.1.4-py36hd09be54_0 ...
    installing: cython-0.27.3-py36h1860423_0 ...
    installing: datashape-0.5.4-py36h3ad6b5c_0 ...
    installing: distributed-1.20.2-py36_0 ...
    installing: get_terminal_size-1.0.0-haa9412d_0 ...
    installing: gevent-1.2.2-py36h2fe25dc_0 ...
    installing: imageio-2.2.0-py36he555465_0 ...
    installing: isort-4.2.15-py36had401c0_0 ...
    installing: jinja2-2.10-py36ha16c418_0 ...
    installing: jsonschema-2.6.0-py36h006f8b5_0 ...
    installing: jupyter_core-4.4.0-py36h7c827e3_0 ...
    installing: matplotlib-2.1.2-py36h0e671d2_0 ...
    installing: navigator-updater-0.1.0-py36h14770f7_0 ...
    installing: nose-1.3.7-py36hcdf7029_2 ...
    installing: pandas-0.22.0-py36hf484d3e_0 ...
    installing: pango-1.41.0-hd475d92_0 ...
    installing: patsy-0.5.0-py36_0 ...
    installing: pyflakes-1.6.0-py36h7bd6a15_0 ...
    installing: pygments-2.2.0-py36h0d3125c_0 ...
    installing: pytables-3.4.2-py36h3b5282a_2 ...
    installing: pytest-3.3.2-py36_0 ...
    installing: scikit-learn-0.19.1-py36h7aa7ec6_0 ...
    installing: wheel-0.30.0-py36hfd4bba0_1 ...
    installing: astropy-2.0.3-py36h14c3975_0 ...
    installing: bkcharts-0.2-py36h735825a_0 ...
    installing: bokeh-0.12.13-py36h2f9c1c0_0 ...
    installing: flask-0.12.2-py36hb24657c_0 ...
    installing: jupyter_client-5.2.2-py36_0 ...
    installing: nbformat-4.4.0-py36h31c9010_0 ...
    installing: pip-9.0.1-py36h6c6f9ce_4 ...
    installing: prompt_toolkit-1.0.15-py36h17d85b1_0 ...
    installing: pylint-1.8.2-py36_0 ...
    installing: pyopenssl-17.5.0-py36h20ba746_0 ...
    installing: statsmodels-0.8.0-py36h8533d0b_0 ...
    installing: dask-0.16.1-py36_0 ...
    installing: flask-cors-3.0.3-py36h2d857d3_0 ...
    installing: ipython-6.2.1-py36h88c514a_1 ...
    installing: nbconvert-5.3.1-py36hb41ffb7_0 ...
    installing: seaborn-0.8.1-py36hfad7ec4_0 ...
    installing: urllib3-1.22-py36hbe7ace6_0 ...
    installing: ipykernel-4.8.0-py36_0 ...
    installing: odo-0.5.1-py36h90ed295_0 ...
    installing: requests-2.18.4-py36he2e5f8d_1 ...
    installing: scikit-image-0.13.1-py36h14c3975_1 ...
    installing: anaconda-client-1.6.9-py36_0 ...
    installing: blaze-0.11.3-py36h4e06776_0 ...
    installing: jupyter_console-5.2.0-py36he59e554_1 ...
    installing: notebook-5.4.0-py36_0 ...
    installing: qtconsole-4.3.1-py36h8f73b5b_0 ...
    installing: sphinx-1.6.6-py36_0 ...
    installing: anaconda-project-0.8.2-py36h44fb852_0 ...
    installing: jupyterlab_launcher-0.10.2-py36_0 ...
    installing: numpydoc-0.7.0-py36h18f165f_0 ...
    installing: widgetsnbextension-3.1.0-py36_0 ...
    installing: anaconda-navigator-1.7.0-py36_0 ...
    installing: ipywidgets-7.1.1-py36_0 ...
    installing: jupyterlab-0.31.5-py36_0 ...
    installing: spyder-3.2.6-py36_0 ...
    installing: _ipyw_jlab_nb_ext_conf-0.1.0-py36he11e457_0 ...
    installing: jupyter-1.0.0-py36_4 ...
    installing: anaconda-5.1.0-py36_2 ...
    installing: conda-4.4.10-py36_0 ...
    installing: conda-build-3.4.1-py36_0 ...
    installation finished.
    WARNING:
        You currently have a PYTHONPATH environment variable set. This may cause
        unexpected behavior when running the Python interpreter in Anaconda3.
        For best results, please verify that your PYTHONPATH only points to
        directories of packages that are compatible with the Python interpreter
        in Anaconda3: /usr/local
    Solving environment: - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / done
    
    
    ==> WARNING: A newer version of conda exists. <==
      current version: 4.4.10
      latest version: 4.8.4
    
    Please update conda by running
    
        $ conda update -n base conda
    
    
    
    ## Package Plan ##
    
      environment location: /usr/local
    
      added / updated specs: 
        - cudatoolkit=10.0
        - pytorch
        - torchvision
    
    
    The following packages will be downloaded:
    
        package                    |            build
        ---------------------------|-----------------
        libgcc-ng-9.1.0            |       hdf63c60_0         8.1 MB
        libpng-1.6.37              |       hbc83047_0         364 KB
        ninja-1.8.2                |   py36h6bb024c_1         1.3 MB
        openssl-1.0.2u             |       h7b6447c_0         3.1 MB
        torchvision-0.5.0          |       py36_cu100         9.1 MB  pytorch
        blas-1.0                   |              mkl           6 KB
        setuptools-49.6.0          |           py36_0         927 KB
        tk-8.6.10                  |       hbc83047_0         3.2 MB
        zlib-1.2.11                |       h7b6447c_3         120 KB
        python-3.6.6               |       hc3d631a_0        29.4 MB
        wheel-0.34.2               |           py36_0          49 KB
        ncurses-6.1                |       hf484d3e_0         943 KB
        readline-7.0               |       h7b6447c_5         392 KB
        libtiff-4.0.9              |       he85c1e1_1         566 KB
        certifi-2020.6.20          |           py36_0         160 KB
        libedit-3.1.20181209       |       hc058e9b_0         188 KB
        freetype-2.10.2            |       h5ab3b9f_0         915 KB
        numpy-1.14.2               |   py36hdbf6ddf_0         4.0 MB
        xz-5.2.5                   |       h7b6447c_0         438 KB
        six-1.15.0                 |             py_0          13 KB
        pillow-5.4.1               |   py36h34e0f95_0         627 KB
        olefile-0.46               |             py_0          33 KB
        pytorch-1.4.0              |py3.6_cuda10.0.130_cudnn7.6.3_0       422.5 MB  pytorch
        pip-20.2.2                 |           py36_0         2.0 MB
        ca-certificates-2020.6.24  |                0         133 KB
        _libgcc_mutex-0.1          |             main           3 KB
        cudatoolkit-10.0.130       |                0       380.0 MB
        sqlite-3.31.1              |       h7b6447c_0         2.0 MB
        ------------------------------------------------------------
                                               Total:       870.6 MB
    
    The following NEW packages will be INSTALLED:
    
        _libgcc_mutex:   0.1-main                                     
        blas:            1.0-mkl                                      
        cudatoolkit:     10.0.130-0                                   
        ninja:           1.8.2-py36h6bb024c_1                         
        pytorch:         1.4.0-py3.6_cuda10.0.130_cudnn7.6.3_0 pytorch
        torchvision:     0.5.0-py36_cu100                      pytorch
    
    The following packages will be UPDATED:
    
        ca-certificates: 2017.08.26-h1d4fec5_0                         --> 2020.6.24-0            
        certifi:         2018.1.18-py36_0                              --> 2020.6.20-py36_0       
        freetype:        2.8-hab7d2ae_1                                --> 2.10.2-h5ab3b9f_0      
        libedit:         3.1-heed3624_0                                --> 3.1.20181209-hc058e9b_0
        libgcc-ng:       7.2.0-h7cc24e2_2                              --> 9.1.0-hdf63c60_0       
        libpng:          1.6.34-hb9fc6fc_0                             --> 1.6.37-hbc83047_0      
        libtiff:         4.0.9-h28f6b97_0                              --> 4.0.9-he85c1e1_1       
        ncurses:         6.0-h9df7e31_2                                --> 6.1-hf484d3e_0         
        numpy:           1.14.0-py36h3dfced4_1                         --> 1.14.2-py36hdbf6ddf_0  
        olefile:         0.45.1-py36_0                                 --> 0.46-py_0              
        openssl:         1.0.2n-hb7f436b_0                             --> 1.0.2u-h7b6447c_0      
        pillow:          5.0.0-py36h3deb7b8_0                          --> 5.4.1-py36h34e0f95_0   
        pip:             9.0.1-py36h6c6f9ce_4                          --> 20.2.2-py36_0          
        python:          3.6.4-hc3d631a_1                              --> 3.6.6-hc3d631a_0       
        readline:        7.0-ha6073c6_4                                --> 7.0-h7b6447c_5         
        setuptools:      38.4.0-py36_0                                 --> 49.6.0-py36_0          
        six:             1.11.0-py36h372c433_1                         --> 1.15.0-py_0            
        sqlite:          3.22.0-h1bed415_0                             --> 3.31.1-h7b6447c_0      
        tk:              8.6.7-hc745277_3                              --> 8.6.10-hbc83047_0      
        wheel:           0.30.0-py36hfd4bba0_1                         --> 0.34.2-py36_0          
        xz:              5.2.3-h55aa19d_2                              --> 5.2.5-h7b6447c_0       
        zlib:            1.2.11-ha838bed_2                             --> 1.2.11-h7b6447c_3      
    
    
    Downloading and Extracting Packages
    libgcc-ng 9.1.0: 100% 1.0/1 [00:02<00:00,  2.14s/it]               
    libpng 1.6.37: 100% 1.0/1 [00:00<00:00,  6.70it/s]               
    ninja 1.8.2: 100% 1.0/1 [00:00<00:00,  2.47it/s] 
    openssl 1.0.2u: 100% 1.0/1 [00:00<00:00,  1.04it/s]               
    torchvision 0.5.0: 100% 1.0/1 [00:03<00:00,  3.63s/it]               
    blas 1.0: 100% 1.0/1 [00:00<00:00, 21.68it/s]
    setuptools 49.6.0: 100% 1.0/1 [00:00<00:00,  2.32it/s]               
    tk 8.6.10: 100% 1.0/1 [00:01<00:00,  1.06s/it]               
    zlib 1.2.11: 100% 1.0/1 [00:00<00:00, 14.22it/s]
    python 3.6.6: 100% 1.0/1 [00:07<00:00,  7.01s/it]               
    wheel 0.34.2: 100% 1.0/1 [00:00<00:00, 15.26it/s]
    ncurses 6.1: 100% 1.0/1 [00:00<00:00,  1.18it/s]               
    readline 7.0: 100% 1.0/1 [00:00<00:00,  5.46it/s] 
    libtiff 4.0.9: 100% 1.0/1 [00:00<00:00,  4.40it/s] 
    certifi 2020.6.20: 100% 1.0/1 [00:00<00:00, 12.93it/s]
    libedit 3.1.20181209: 100% 1.0/1 [00:00<00:00,  9.27it/s]               
    freetype 2.10.2: 100% 1.0/1 [00:00<00:00,  2.84it/s]               
    numpy 1.14.2: 100% 1.0/1 [00:01<00:00,  1.58s/it]               
    xz 5.2.5: 100% 1.0/1 [00:00<00:00,  5.20it/s] 
    six 1.15.0: 100% 1.0/1 [00:00<00:00, 24.45it/s]
    pillow 5.4.1: 100% 1.0/1 [00:00<00:00,  3.92it/s]               
    olefile 0.46: 100% 1.0/1 [00:00<00:00, 14.63it/s]
    pytorch 1.4.0: 100% 1.0/1 [01:53<00:00, 113.35s/it]               
    pip 20.2.2: 100% 1.0/1 [00:00<00:00,  1.14it/s]              
    ca-certificates 2020.6.24: 100% 1.0/1 [00:00<00:00, 12.73it/s]
    _libgcc_mutex 0.1: 100% 1.0/1 [00:00<00:00, 24.90it/s]
    cudatoolkit 10.0.130: 100% 1.0/1 [01:26<00:00, 86.27s/it]                 
    sqlite 3.31.1: 100% 1.0/1 [00:00<00:00,  1.62it/s]    
    Preparing transaction: \ | / - done
    Verifying transaction: | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ | / - \ done
    Executing transaction: / - \ | / - \ | / - \ | / done
    
    PackagesNotFoundError: The following packages are not available from current channels:
    
      - moviepy
      - opencv-python
      - tflib
    
    Current channels:
    
      - https://repo.continuum.io/pkgs/main/linux-64
      - https://repo.continuum.io/pkgs/main/noarch
      - https://repo.continuum.io/pkgs/free/linux-64
      - https://repo.continuum.io/pkgs/free/noarch
      - https://repo.continuum.io/pkgs/r/linux-64
      - https://repo.continuum.io/pkgs/r/noarch
      - https://repo.continuum.io/pkgs/pro/linux-64
      - https://repo.continuum.io/pkgs/pro/noarch
    
    
    


```python
%%writefile setup.sh

git clone https://github.com/NVIDIA/apex
cd apex
pip install -v --no-cache-dir ./
```

    Writing setup.sh
    


```python
! mv DeepPrivacy/deep_privacy . && mkdir -p models/large/checkpoints && mv DeepPrivacy/models/isvc_large/config.yml models/large
# Download checkpoint and save it to models/large/checkpoints
```


```python
!sh setup.sh
```

    Cloning into 'apex'...
    remote: Enumerating objects: 7431, done.[K
    remote: Total 7431 (delta 0), reused 0 (delta 0), pack-reused 7431[K
    Receiving objects: 100% (7431/7431), 13.90 MiB | 7.33 MiB/s, done.
    Resolving deltas: 100% (5022/5022), done.
    Created temporary directory: /tmp/pip-ephem-wheel-cache-u1piuhr8
    Created temporary directory: /tmp/pip-req-tracker-5o9btbxy
    Created requirements tracker '/tmp/pip-req-tracker-5o9btbxy'
    Created temporary directory: /tmp/pip-install-nqu7bno0
    Processing /content/apex
      Created temporary directory: /tmp/pip-req-build-4ehxv_ht
      Added file:///content/apex to build tracker '/tmp/pip-req-tracker-5o9btbxy'
        Running setup.py (path:/tmp/pip-req-build-4ehxv_ht/setup.py) egg_info for package from file:///content/apex
        Running command python setup.py egg_info
    
    
        torch.__version__  = 1.6.0+cu101
    
    
        running egg_info
        creating /tmp/pip-req-build-4ehxv_ht/pip-egg-info/apex.egg-info
        writing /tmp/pip-req-build-4ehxv_ht/pip-egg-info/apex.egg-info/PKG-INFO
        writing dependency_links to /tmp/pip-req-build-4ehxv_ht/pip-egg-info/apex.egg-info/dependency_links.txt
        writing top-level names to /tmp/pip-req-build-4ehxv_ht/pip-egg-info/apex.egg-info/top_level.txt
        writing manifest file '/tmp/pip-req-build-4ehxv_ht/pip-egg-info/apex.egg-info/SOURCES.txt'
        writing manifest file '/tmp/pip-req-build-4ehxv_ht/pip-egg-info/apex.egg-info/SOURCES.txt'
        /tmp/pip-req-build-4ehxv_ht/setup.py:67: UserWarning: Option --pyprof not specified. Not installing PyProf dependencies!
          warnings.warn("Option --pyprof not specified. Not installing PyProf dependencies!")
      Source in /tmp/pip-req-build-4ehxv_ht has version 0.1, which satisfies requirement apex==0.1 from file:///content/apex
      Removed apex==0.1 from file:///content/apex from build tracker '/tmp/pip-req-tracker-5o9btbxy'
    Building wheels for collected packages: apex
      Created temporary directory: /tmp/pip-wheel-8vcnnwcn
      Building wheel for apex (setup.py) ... [?25l  Destination directory: /tmp/pip-wheel-8vcnnwcn
      Running command /usr/bin/python3 -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/tmp/pip-req-build-4ehxv_ht/setup.py'"'"'; __file__='"'"'/tmp/pip-req-build-4ehxv_ht/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' bdist_wheel -d /tmp/pip-wheel-8vcnnwcn --python-tag cp36
    
    
      torch.__version__  = 1.6.0+cu101
    
    
      /tmp/pip-req-build-4ehxv_ht/setup.py:67: UserWarning: Option --pyprof not specified. Not installing PyProf dependencies!
        warnings.warn("Option --pyprof not specified. Not installing PyProf dependencies!")
      running bdist_wheel
      running build
      running build_py
      creating build
      creating build/lib
      creating build/lib/apex
      copying apex/__init__.py -> build/lib/apex
      creating build/lib/apex/pyprof
      copying apex/pyprof/__init__.py -> build/lib/apex/pyprof
      creating build/lib/apex/parallel
      copying apex/parallel/sync_batchnorm_kernel.py -> build/lib/apex/parallel
      copying apex/parallel/optimized_sync_batchnorm_kernel.py -> build/lib/apex/parallel
      copying apex/parallel/sync_batchnorm.py -> build/lib/apex/parallel
      copying apex/parallel/LARC.py -> build/lib/apex/parallel
      copying apex/parallel/optimized_sync_batchnorm.py -> build/lib/apex/parallel
      copying apex/parallel/distributed.py -> build/lib/apex/parallel
      copying apex/parallel/__init__.py -> build/lib/apex/parallel
      copying apex/parallel/multiproc.py -> build/lib/apex/parallel
      creating build/lib/apex/contrib
      copying apex/contrib/__init__.py -> build/lib/apex/contrib
      creating build/lib/apex/multi_tensor_apply
      copying apex/multi_tensor_apply/__init__.py -> build/lib/apex/multi_tensor_apply
      copying apex/multi_tensor_apply/multi_tensor_apply.py -> build/lib/apex/multi_tensor_apply
      creating build/lib/apex/reparameterization
      copying apex/reparameterization/reparameterization.py -> build/lib/apex/reparameterization
      copying apex/reparameterization/weight_norm.py -> build/lib/apex/reparameterization
      copying apex/reparameterization/__init__.py -> build/lib/apex/reparameterization
      creating build/lib/apex/normalization
      copying apex/normalization/fused_layer_norm.py -> build/lib/apex/normalization
      copying apex/normalization/__init__.py -> build/lib/apex/normalization
      creating build/lib/apex/RNN
      copying apex/RNN/cells.py -> build/lib/apex/RNN
      copying apex/RNN/RNNBackend.py -> build/lib/apex/RNN
      copying apex/RNN/__init__.py -> build/lib/apex/RNN
      copying apex/RNN/models.py -> build/lib/apex/RNN
      creating build/lib/apex/fp16_utils
      copying apex/fp16_utils/fp16util.py -> build/lib/apex/fp16_utils
      copying apex/fp16_utils/loss_scaler.py -> build/lib/apex/fp16_utils
      copying apex/fp16_utils/fp16_optimizer.py -> build/lib/apex/fp16_utils
      copying apex/fp16_utils/__init__.py -> build/lib/apex/fp16_utils
      creating build/lib/apex/optimizers
      copying apex/optimizers/fused_sgd.py -> build/lib/apex/optimizers
      copying apex/optimizers/fused_novograd.py -> build/lib/apex/optimizers
      copying apex/optimizers/__init__.py -> build/lib/apex/optimizers
      copying apex/optimizers/fused_lamb.py -> build/lib/apex/optimizers
      copying apex/optimizers/fused_adam.py -> build/lib/apex/optimizers
      copying apex/optimizers/fused_adagrad.py -> build/lib/apex/optimizers
      creating build/lib/apex/amp
      copying apex/amp/_amp_state.py -> build/lib/apex/amp
      copying apex/amp/utils.py -> build/lib/apex/amp
      copying apex/amp/_initialize.py -> build/lib/apex/amp
      copying apex/amp/compat.py -> build/lib/apex/amp
      copying apex/amp/__version__.py -> build/lib/apex/amp
      copying apex/amp/handle.py -> build/lib/apex/amp
      copying apex/amp/amp.py -> build/lib/apex/amp
      copying apex/amp/wrap.py -> build/lib/apex/amp
      copying apex/amp/__init__.py -> build/lib/apex/amp
      copying apex/amp/frontend.py -> build/lib/apex/amp
      copying apex/amp/_process_optimizer.py -> build/lib/apex/amp
      copying apex/amp/rnn_compat.py -> build/lib/apex/amp
      copying apex/amp/scaler.py -> build/lib/apex/amp
      copying apex/amp/opt.py -> build/lib/apex/amp
      creating build/lib/apex/mlp
      copying apex/mlp/mlp.py -> build/lib/apex/mlp
      copying apex/mlp/__init__.py -> build/lib/apex/mlp
      creating build/lib/apex/pyprof/prof
      copying apex/pyprof/prof/pointwise.py -> build/lib/apex/pyprof/prof
      copying apex/pyprof/prof/activation.py -> build/lib/apex/pyprof/prof
      copying apex/pyprof/prof/reduction.py -> build/lib/apex/pyprof/prof
      copying apex/pyprof/prof/data.py -> build/lib/apex/pyprof/prof
      copying apex/pyprof/prof/blas.py -> build/lib/apex/pyprof/prof
      copying apex/pyprof/prof/base.py -> build/lib/apex/pyprof/prof
      copying apex/pyprof/prof/__main__.py -> build/lib/apex/pyprof/prof
      copying apex/pyprof/prof/convert.py -> build/lib/apex/pyprof/prof
      copying apex/pyprof/prof/prof.py -> build/lib/apex/pyprof/prof
      copying apex/pyprof/prof/randomSample.py -> build/lib/apex/pyprof/prof
      copying apex/pyprof/prof/embedding.py -> build/lib/apex/pyprof/prof
      copying apex/pyprof/prof/recurrentCell.py -> build/lib/apex/pyprof/prof
      copying apex/pyprof/prof/usage.py -> build/lib/apex/pyprof/prof
      copying apex/pyprof/prof/utility.py -> build/lib/apex/pyprof/prof
      copying apex/pyprof/prof/dropout.py -> build/lib/apex/pyprof/prof
      copying apex/pyprof/prof/pooling.py -> build/lib/apex/pyprof/prof
      copying apex/pyprof/prof/output.py -> build/lib/apex/pyprof/prof
      copying apex/pyprof/prof/index_slice_join_mutate.py -> build/lib/apex/pyprof/prof
      copying apex/pyprof/prof/__init__.py -> build/lib/apex/pyprof/prof
      copying apex/pyprof/prof/misc.py -> build/lib/apex/pyprof/prof
      copying apex/pyprof/prof/linear.py -> build/lib/apex/pyprof/prof
      copying apex/pyprof/prof/loss.py -> build/lib/apex/pyprof/prof
      copying apex/pyprof/prof/optim.py -> build/lib/apex/pyprof/prof
      copying apex/pyprof/prof/conv.py -> build/lib/apex/pyprof/prof
      copying apex/pyprof/prof/softmax.py -> build/lib/apex/pyprof/prof
      copying apex/pyprof/prof/normalization.py -> build/lib/apex/pyprof/prof
      creating build/lib/apex/pyprof/nvtx
      copying apex/pyprof/nvtx/nvmarker.py -> build/lib/apex/pyprof/nvtx
      copying apex/pyprof/nvtx/__init__.py -> build/lib/apex/pyprof/nvtx
      creating build/lib/apex/pyprof/parse
      copying apex/pyprof/parse/__main__.py -> build/lib/apex/pyprof/parse
      copying apex/pyprof/parse/nvvp.py -> build/lib/apex/pyprof/parse
      copying apex/pyprof/parse/parse.py -> build/lib/apex/pyprof/parse
      copying apex/pyprof/parse/db.py -> build/lib/apex/pyprof/parse
      copying apex/pyprof/parse/__init__.py -> build/lib/apex/pyprof/parse
      copying apex/pyprof/parse/kernel.py -> build/lib/apex/pyprof/parse
      creating build/lib/apex/contrib/groupbn
      copying apex/contrib/groupbn/batch_norm.py -> build/lib/apex/contrib/groupbn
      copying apex/contrib/groupbn/__init__.py -> build/lib/apex/contrib/groupbn
      creating build/lib/apex/contrib/xentropy
      copying apex/contrib/xentropy/softmax_xentropy.py -> build/lib/apex/contrib/xentropy
      copying apex/contrib/xentropy/__init__.py -> build/lib/apex/contrib/xentropy
      creating build/lib/apex/contrib/multihead_attn
      copying apex/contrib/multihead_attn/encdec_multihead_attn_func.py -> build/lib/apex/contrib/multihead_attn
      copying apex/contrib/multihead_attn/fast_self_multihead_attn_func.py -> build/lib/apex/contrib/multihead_attn
      copying apex/contrib/multihead_attn/fast_encdec_multihead_attn_func.py -> build/lib/apex/contrib/multihead_attn
      copying apex/contrib/multihead_attn/fast_encdec_multihead_attn_norm_add_func.py -> build/lib/apex/contrib/multihead_attn
      copying apex/contrib/multihead_attn/mask_softmax_dropout_func.py -> build/lib/apex/contrib/multihead_attn
      copying apex/contrib/multihead_attn/encdec_multihead_attn.py -> build/lib/apex/contrib/multihead_attn
      copying apex/contrib/multihead_attn/__init__.py -> build/lib/apex/contrib/multihead_attn
      copying apex/contrib/multihead_attn/fast_self_multihead_attn_norm_add_func.py -> build/lib/apex/contrib/multihead_attn
      copying apex/contrib/multihead_attn/self_multihead_attn.py -> build/lib/apex/contrib/multihead_attn
      copying apex/contrib/multihead_attn/self_multihead_attn_func.py -> build/lib/apex/contrib/multihead_attn
      creating build/lib/apex/contrib/sparsity
      copying apex/contrib/sparsity/asp.py -> build/lib/apex/contrib/sparsity
      copying apex/contrib/sparsity/__init__.py -> build/lib/apex/contrib/sparsity
      copying apex/contrib/sparsity/sparse_masklib.py -> build/lib/apex/contrib/sparsity
      creating build/lib/apex/contrib/optimizers
      copying apex/contrib/optimizers/distributed_fused_lamb.py -> build/lib/apex/contrib/optimizers
      copying apex/contrib/optimizers/fused_sgd.py -> build/lib/apex/contrib/optimizers
      copying apex/contrib/optimizers/distributed_fused_adam_v3.py -> build/lib/apex/contrib/optimizers
      copying apex/contrib/optimizers/fp16_optimizer.py -> build/lib/apex/contrib/optimizers
      copying apex/contrib/optimizers/distributed_fused_adam_v2.py -> build/lib/apex/contrib/optimizers
      copying apex/contrib/optimizers/__init__.py -> build/lib/apex/contrib/optimizers
      copying apex/contrib/optimizers/distributed_fused_adam.py -> build/lib/apex/contrib/optimizers
      copying apex/contrib/optimizers/fused_lamb.py -> build/lib/apex/contrib/optimizers
      copying apex/contrib/optimizers/fused_adam.py -> build/lib/apex/contrib/optimizers
      creating build/lib/apex/amp/lists
      copying apex/amp/lists/functional_overrides.py -> build/lib/apex/amp/lists
      copying apex/amp/lists/tensor_overrides.py -> build/lib/apex/amp/lists
      copying apex/amp/lists/__init__.py -> build/lib/apex/amp/lists
      copying apex/amp/lists/torch_overrides.py -> build/lib/apex/amp/lists
      installing to build/bdist.linux-x86_64/wheel
      running install
      running install_lib
      creating build/bdist.linux-x86_64
      creating build/bdist.linux-x86_64/wheel
      creating build/bdist.linux-x86_64/wheel/apex
      creating build/bdist.linux-x86_64/wheel/apex/pyprof
      creating build/bdist.linux-x86_64/wheel/apex/pyprof/prof
      copying build/lib/apex/pyprof/prof/pointwise.py -> build/bdist.linux-x86_64/wheel/apex/pyprof/prof
      copying build/lib/apex/pyprof/prof/activation.py -> build/bdist.linux-x86_64/wheel/apex/pyprof/prof
      copying build/lib/apex/pyprof/prof/reduction.py -> build/bdist.linux-x86_64/wheel/apex/pyprof/prof
      copying build/lib/apex/pyprof/prof/data.py -> build/bdist.linux-x86_64/wheel/apex/pyprof/prof
      copying build/lib/apex/pyprof/prof/blas.py -> build/bdist.linux-x86_64/wheel/apex/pyprof/prof
      copying build/lib/apex/pyprof/prof/base.py -> build/bdist.linux-x86_64/wheel/apex/pyprof/prof
      copying build/lib/apex/pyprof/prof/__main__.py -> build/bdist.linux-x86_64/wheel/apex/pyprof/prof
      copying build/lib/apex/pyprof/prof/convert.py -> build/bdist.linux-x86_64/wheel/apex/pyprof/prof
      copying build/lib/apex/pyprof/prof/prof.py -> build/bdist.linux-x86_64/wheel/apex/pyprof/prof
      copying build/lib/apex/pyprof/prof/randomSample.py -> build/bdist.linux-x86_64/wheel/apex/pyprof/prof
      copying build/lib/apex/pyprof/prof/embedding.py -> build/bdist.linux-x86_64/wheel/apex/pyprof/prof
      copying build/lib/apex/pyprof/prof/recurrentCell.py -> build/bdist.linux-x86_64/wheel/apex/pyprof/prof
      copying build/lib/apex/pyprof/prof/usage.py -> build/bdist.linux-x86_64/wheel/apex/pyprof/prof
      copying build/lib/apex/pyprof/prof/utility.py -> build/bdist.linux-x86_64/wheel/apex/pyprof/prof
      copying build/lib/apex/pyprof/prof/dropout.py -> build/bdist.linux-x86_64/wheel/apex/pyprof/prof
      copying build/lib/apex/pyprof/prof/pooling.py -> build/bdist.linux-x86_64/wheel/apex/pyprof/prof
      copying build/lib/apex/pyprof/prof/output.py -> build/bdist.linux-x86_64/wheel/apex/pyprof/prof
      copying build/lib/apex/pyprof/prof/index_slice_join_mutate.py -> build/bdist.linux-x86_64/wheel/apex/pyprof/prof
      copying build/lib/apex/pyprof/prof/__init__.py -> build/bdist.linux-x86_64/wheel/apex/pyprof/prof
      copying build/lib/apex/pyprof/prof/misc.py -> build/bdist.linux-x86_64/wheel/apex/pyprof/prof
      copying build/lib/apex/pyprof/prof/linear.py -> build/bdist.linux-x86_64/wheel/apex/pyprof/prof
      copying build/lib/apex/pyprof/prof/loss.py -> build/bdist.linux-x86_64/wheel/apex/pyprof/prof
      copying build/lib/apex/pyprof/prof/optim.py -> build/bdist.linux-x86_64/wheel/apex/pyprof/prof
      copying build/lib/apex/pyprof/prof/conv.py -> build/bdist.linux-x86_64/wheel/apex/pyprof/prof
      copying build/lib/apex/pyprof/prof/softmax.py -> build/bdist.linux-x86_64/wheel/apex/pyprof/prof
      copying build/lib/apex/pyprof/prof/normalization.py -> build/bdist.linux-x86_64/wheel/apex/pyprof/prof
      copying build/lib/apex/pyprof/__init__.py -> build/bdist.linux-x86_64/wheel/apex/pyprof
      creating build/bdist.linux-x86_64/wheel/apex/pyprof/nvtx
      copying build/lib/apex/pyprof/nvtx/nvmarker.py -> build/bdist.linux-x86_64/wheel/apex/pyprof/nvtx
      copying build/lib/apex/pyprof/nvtx/__init__.py -> build/bdist.linux-x86_64/wheel/apex/pyprof/nvtx
      creating build/bdist.linux-x86_64/wheel/apex/pyprof/parse
      copying build/lib/apex/pyprof/parse/__main__.py -> build/bdist.linux-x86_64/wheel/apex/pyprof/parse
      copying build/lib/apex/pyprof/parse/nvvp.py -> build/bdist.linux-x86_64/wheel/apex/pyprof/parse
      copying build/lib/apex/pyprof/parse/parse.py -> build/bdist.linux-x86_64/wheel/apex/pyprof/parse
      copying build/lib/apex/pyprof/parse/db.py -> build/bdist.linux-x86_64/wheel/apex/pyprof/parse
      copying build/lib/apex/pyprof/parse/__init__.py -> build/bdist.linux-x86_64/wheel/apex/pyprof/parse
      copying build/lib/apex/pyprof/parse/kernel.py -> build/bdist.linux-x86_64/wheel/apex/pyprof/parse
      creating build/bdist.linux-x86_64/wheel/apex/parallel
      copying build/lib/apex/parallel/sync_batchnorm_kernel.py -> build/bdist.linux-x86_64/wheel/apex/parallel
      copying build/lib/apex/parallel/optimized_sync_batchnorm_kernel.py -> build/bdist.linux-x86_64/wheel/apex/parallel
      copying build/lib/apex/parallel/sync_batchnorm.py -> build/bdist.linux-x86_64/wheel/apex/parallel
      copying build/lib/apex/parallel/LARC.py -> build/bdist.linux-x86_64/wheel/apex/parallel
      copying build/lib/apex/parallel/optimized_sync_batchnorm.py -> build/bdist.linux-x86_64/wheel/apex/parallel
      copying build/lib/apex/parallel/distributed.py -> build/bdist.linux-x86_64/wheel/apex/parallel
      copying build/lib/apex/parallel/__init__.py -> build/bdist.linux-x86_64/wheel/apex/parallel
      copying build/lib/apex/parallel/multiproc.py -> build/bdist.linux-x86_64/wheel/apex/parallel
      creating build/bdist.linux-x86_64/wheel/apex/contrib
      creating build/bdist.linux-x86_64/wheel/apex/contrib/groupbn
      copying build/lib/apex/contrib/groupbn/batch_norm.py -> build/bdist.linux-x86_64/wheel/apex/contrib/groupbn
      copying build/lib/apex/contrib/groupbn/__init__.py -> build/bdist.linux-x86_64/wheel/apex/contrib/groupbn
      creating build/bdist.linux-x86_64/wheel/apex/contrib/xentropy
      copying build/lib/apex/contrib/xentropy/softmax_xentropy.py -> build/bdist.linux-x86_64/wheel/apex/contrib/xentropy
      copying build/lib/apex/contrib/xentropy/__init__.py -> build/bdist.linux-x86_64/wheel/apex/contrib/xentropy
      copying build/lib/apex/contrib/__init__.py -> build/bdist.linux-x86_64/wheel/apex/contrib
      creating build/bdist.linux-x86_64/wheel/apex/contrib/multihead_attn
      copying build/lib/apex/contrib/multihead_attn/encdec_multihead_attn_func.py -> build/bdist.linux-x86_64/wheel/apex/contrib/multihead_attn
      copying build/lib/apex/contrib/multihead_attn/fast_self_multihead_attn_func.py -> build/bdist.linux-x86_64/wheel/apex/contrib/multihead_attn
      copying build/lib/apex/contrib/multihead_attn/fast_encdec_multihead_attn_func.py -> build/bdist.linux-x86_64/wheel/apex/contrib/multihead_attn
      copying build/lib/apex/contrib/multihead_attn/fast_encdec_multihead_attn_norm_add_func.py -> build/bdist.linux-x86_64/wheel/apex/contrib/multihead_attn
      copying build/lib/apex/contrib/multihead_attn/mask_softmax_dropout_func.py -> build/bdist.linux-x86_64/wheel/apex/contrib/multihead_attn
      copying build/lib/apex/contrib/multihead_attn/encdec_multihead_attn.py -> build/bdist.linux-x86_64/wheel/apex/contrib/multihead_attn
      copying build/lib/apex/contrib/multihead_attn/__init__.py -> build/bdist.linux-x86_64/wheel/apex/contrib/multihead_attn
      copying build/lib/apex/contrib/multihead_attn/fast_self_multihead_attn_norm_add_func.py -> build/bdist.linux-x86_64/wheel/apex/contrib/multihead_attn
      copying build/lib/apex/contrib/multihead_attn/self_multihead_attn.py -> build/bdist.linux-x86_64/wheel/apex/contrib/multihead_attn
      copying build/lib/apex/contrib/multihead_attn/self_multihead_attn_func.py -> build/bdist.linux-x86_64/wheel/apex/contrib/multihead_attn
      creating build/bdist.linux-x86_64/wheel/apex/contrib/sparsity
      copying build/lib/apex/contrib/sparsity/asp.py -> build/bdist.linux-x86_64/wheel/apex/contrib/sparsity
      copying build/lib/apex/contrib/sparsity/__init__.py -> build/bdist.linux-x86_64/wheel/apex/contrib/sparsity
      copying build/lib/apex/contrib/sparsity/sparse_masklib.py -> build/bdist.linux-x86_64/wheel/apex/contrib/sparsity
      creating build/bdist.linux-x86_64/wheel/apex/contrib/optimizers
      copying build/lib/apex/contrib/optimizers/distributed_fused_lamb.py -> build/bdist.linux-x86_64/wheel/apex/contrib/optimizers
      copying build/lib/apex/contrib/optimizers/fused_sgd.py -> build/bdist.linux-x86_64/wheel/apex/contrib/optimizers
      copying build/lib/apex/contrib/optimizers/distributed_fused_adam_v3.py -> build/bdist.linux-x86_64/wheel/apex/contrib/optimizers
      copying build/lib/apex/contrib/optimizers/fp16_optimizer.py -> build/bdist.linux-x86_64/wheel/apex/contrib/optimizers
      copying build/lib/apex/contrib/optimizers/distributed_fused_adam_v2.py -> build/bdist.linux-x86_64/wheel/apex/contrib/optimizers
      copying build/lib/apex/contrib/optimizers/__init__.py -> build/bdist.linux-x86_64/wheel/apex/contrib/optimizers
      copying build/lib/apex/contrib/optimizers/distributed_fused_adam.py -> build/bdist.linux-x86_64/wheel/apex/contrib/optimizers
      copying build/lib/apex/contrib/optimizers/fused_lamb.py -> build/bdist.linux-x86_64/wheel/apex/contrib/optimizers
      copying build/lib/apex/contrib/optimizers/fused_adam.py -> build/bdist.linux-x86_64/wheel/apex/contrib/optimizers
      creating build/bdist.linux-x86_64/wheel/apex/multi_tensor_apply
      copying build/lib/apex/multi_tensor_apply/__init__.py -> build/bdist.linux-x86_64/wheel/apex/multi_tensor_apply
      copying build/lib/apex/multi_tensor_apply/multi_tensor_apply.py -> build/bdist.linux-x86_64/wheel/apex/multi_tensor_apply
      creating build/bdist.linux-x86_64/wheel/apex/reparameterization
      copying build/lib/apex/reparameterization/reparameterization.py -> build/bdist.linux-x86_64/wheel/apex/reparameterization
      copying build/lib/apex/reparameterization/weight_norm.py -> build/bdist.linux-x86_64/wheel/apex/reparameterization
      copying build/lib/apex/reparameterization/__init__.py -> build/bdist.linux-x86_64/wheel/apex/reparameterization
      copying build/lib/apex/__init__.py -> build/bdist.linux-x86_64/wheel/apex
      creating build/bdist.linux-x86_64/wheel/apex/normalization
      copying build/lib/apex/normalization/fused_layer_norm.py -> build/bdist.linux-x86_64/wheel/apex/normalization
      copying build/lib/apex/normalization/__init__.py -> build/bdist.linux-x86_64/wheel/apex/normalization
      creating build/bdist.linux-x86_64/wheel/apex/RNN
      copying build/lib/apex/RNN/cells.py -> build/bdist.linux-x86_64/wheel/apex/RNN
      copying build/lib/apex/RNN/RNNBackend.py -> build/bdist.linux-x86_64/wheel/apex/RNN
      copying build/lib/apex/RNN/__init__.py -> build/bdist.linux-x86_64/wheel/apex/RNN
      copying build/lib/apex/RNN/models.py -> build/bdist.linux-x86_64/wheel/apex/RNN
      creating build/bdist.linux-x86_64/wheel/apex/fp16_utils
      copying build/lib/apex/fp16_utils/fp16util.py -> build/bdist.linux-x86_64/wheel/apex/fp16_utils
      copying build/lib/apex/fp16_utils/loss_scaler.py -> build/bdist.linux-x86_64/wheel/apex/fp16_utils
      copying build/lib/apex/fp16_utils/fp16_optimizer.py -> build/bdist.linux-x86_64/wheel/apex/fp16_utils
      copying build/lib/apex/fp16_utils/__init__.py -> build/bdist.linux-x86_64/wheel/apex/fp16_utils
      creating build/bdist.linux-x86_64/wheel/apex/optimizers
      copying build/lib/apex/optimizers/fused_sgd.py -> build/bdist.linux-x86_64/wheel/apex/optimizers
      copying build/lib/apex/optimizers/fused_novograd.py -> build/bdist.linux-x86_64/wheel/apex/optimizers
      copying build/lib/apex/optimizers/__init__.py -> build/bdist.linux-x86_64/wheel/apex/optimizers
      copying build/lib/apex/optimizers/fused_lamb.py -> build/bdist.linux-x86_64/wheel/apex/optimizers
      copying build/lib/apex/optimizers/fused_adam.py -> build/bdist.linux-x86_64/wheel/apex/optimizers
      copying build/lib/apex/optimizers/fused_adagrad.py -> build/bdist.linux-x86_64/wheel/apex/optimizers
      creating build/bdist.linux-x86_64/wheel/apex/amp
      copying build/lib/apex/amp/_amp_state.py -> build/bdist.linux-x86_64/wheel/apex/amp
      copying build/lib/apex/amp/utils.py -> build/bdist.linux-x86_64/wheel/apex/amp
      copying build/lib/apex/amp/_initialize.py -> build/bdist.linux-x86_64/wheel/apex/amp
      copying build/lib/apex/amp/compat.py -> build/bdist.linux-x86_64/wheel/apex/amp
      copying build/lib/apex/amp/__version__.py -> build/bdist.linux-x86_64/wheel/apex/amp
      copying build/lib/apex/amp/handle.py -> build/bdist.linux-x86_64/wheel/apex/amp
      copying build/lib/apex/amp/amp.py -> build/bdist.linux-x86_64/wheel/apex/amp
      copying build/lib/apex/amp/wrap.py -> build/bdist.linux-x86_64/wheel/apex/amp
      copying build/lib/apex/amp/__init__.py -> build/bdist.linux-x86_64/wheel/apex/amp
      copying build/lib/apex/amp/frontend.py -> build/bdist.linux-x86_64/wheel/apex/amp
      copying build/lib/apex/amp/_process_optimizer.py -> build/bdist.linux-x86_64/wheel/apex/amp
      creating build/bdist.linux-x86_64/wheel/apex/amp/lists
      copying build/lib/apex/amp/lists/functional_overrides.py -> build/bdist.linux-x86_64/wheel/apex/amp/lists
      copying build/lib/apex/amp/lists/tensor_overrides.py -> build/bdist.linux-x86_64/wheel/apex/amp/lists
      copying build/lib/apex/amp/lists/__init__.py -> build/bdist.linux-x86_64/wheel/apex/amp/lists
      copying build/lib/apex/amp/lists/torch_overrides.py -> build/bdist.linux-x86_64/wheel/apex/amp/lists
      copying build/lib/apex/amp/rnn_compat.py -> build/bdist.linux-x86_64/wheel/apex/amp
      copying build/lib/apex/amp/scaler.py -> build/bdist.linux-x86_64/wheel/apex/amp
      copying build/lib/apex/amp/opt.py -> build/bdist.linux-x86_64/wheel/apex/amp
      creating build/bdist.linux-x86_64/wheel/apex/mlp
      copying build/lib/apex/mlp/mlp.py -> build/bdist.linux-x86_64/wheel/apex/mlp
      copying build/lib/apex/mlp/__init__.py -> build/bdist.linux-x86_64/wheel/apex/mlp
      running install_egg_info
      running egg_info
      creating apex.egg-info
      writing apex.egg-info/PKG-INFO
      writing dependency_links to apex.egg-info/dependency_links.txt
      writing top-level names to apex.egg-info/top_level.txt
      writing manifest file 'apex.egg-info/SOURCES.txt'
      writing manifest file 'apex.egg-info/SOURCES.txt'
      Copying apex.egg-info to build/bdist.linux-x86_64/wheel/apex-0.1-py3.6.egg-info
      running install_scripts
      adding license file "LICENSE" (matched pattern "LICEN[CS]E*")
      creating build/bdist.linux-x86_64/wheel/apex-0.1.dist-info/WHEEL
      creating '/tmp/pip-wheel-8vcnnwcn/apex-0.1-cp36-none-any.whl' and adding 'build/bdist.linux-x86_64/wheel' to it
      adding 'apex/__init__.py'
      adding 'apex/RNN/RNNBackend.py'
      adding 'apex/RNN/__init__.py'
      adding 'apex/RNN/cells.py'
      adding 'apex/RNN/models.py'
      adding 'apex/amp/__init__.py'
      adding 'apex/amp/__version__.py'
      adding 'apex/amp/_amp_state.py'
      adding 'apex/amp/_initialize.py'
      adding 'apex/amp/_process_optimizer.py'
      adding 'apex/amp/amp.py'
      adding 'apex/amp/compat.py'
      adding 'apex/amp/frontend.py'
      adding 'apex/amp/handle.py'
      adding 'apex/amp/opt.py'
      adding 'apex/amp/rnn_compat.py'
      adding 'apex/amp/scaler.py'
      adding 'apex/amp/utils.py'
      adding 'apex/amp/wrap.py'
      adding 'apex/amp/lists/__init__.py'
      adding 'apex/amp/lists/functional_overrides.py'
      adding 'apex/amp/lists/tensor_overrides.py'
      adding 'apex/amp/lists/torch_overrides.py'
      adding 'apex/contrib/__init__.py'
      adding 'apex/contrib/groupbn/__init__.py'
      adding 'apex/contrib/groupbn/batch_norm.py'
      adding 'apex/contrib/multihead_attn/__init__.py'
      adding 'apex/contrib/multihead_attn/encdec_multihead_attn.py'
      adding 'apex/contrib/multihead_attn/encdec_multihead_attn_func.py'
      adding 'apex/contrib/multihead_attn/fast_encdec_multihead_attn_func.py'
      adding 'apex/contrib/multihead_attn/fast_encdec_multihead_attn_norm_add_func.py'
      adding 'apex/contrib/multihead_attn/fast_self_multihead_attn_func.py'
      adding 'apex/contrib/multihead_attn/fast_self_multihead_attn_norm_add_func.py'
      adding 'apex/contrib/multihead_attn/mask_softmax_dropout_func.py'
      adding 'apex/contrib/multihead_attn/self_multihead_attn.py'
      adding 'apex/contrib/multihead_attn/self_multihead_attn_func.py'
      adding 'apex/contrib/optimizers/__init__.py'
      adding 'apex/contrib/optimizers/distributed_fused_adam.py'
      adding 'apex/contrib/optimizers/distributed_fused_adam_v2.py'
      adding 'apex/contrib/optimizers/distributed_fused_adam_v3.py'
      adding 'apex/contrib/optimizers/distributed_fused_lamb.py'
      adding 'apex/contrib/optimizers/fp16_optimizer.py'
      adding 'apex/contrib/optimizers/fused_adam.py'
      adding 'apex/contrib/optimizers/fused_lamb.py'
      adding 'apex/contrib/optimizers/fused_sgd.py'
      adding 'apex/contrib/sparsity/__init__.py'
      adding 'apex/contrib/sparsity/asp.py'
      adding 'apex/contrib/sparsity/sparse_masklib.py'
      adding 'apex/contrib/xentropy/__init__.py'
      adding 'apex/contrib/xentropy/softmax_xentropy.py'
      adding 'apex/fp16_utils/__init__.py'
      adding 'apex/fp16_utils/fp16_optimizer.py'
      adding 'apex/fp16_utils/fp16util.py'
      adding 'apex/fp16_utils/loss_scaler.py'
      adding 'apex/mlp/__init__.py'
      adding 'apex/mlp/mlp.py'
      adding 'apex/multi_tensor_apply/__init__.py'
      adding 'apex/multi_tensor_apply/multi_tensor_apply.py'
      adding 'apex/normalization/__init__.py'
      adding 'apex/normalization/fused_layer_norm.py'
      adding 'apex/optimizers/__init__.py'
      adding 'apex/optimizers/fused_adagrad.py'
      adding 'apex/optimizers/fused_adam.py'
      adding 'apex/optimizers/fused_lamb.py'
      adding 'apex/optimizers/fused_novograd.py'
      adding 'apex/optimizers/fused_sgd.py'
      adding 'apex/parallel/LARC.py'
      adding 'apex/parallel/__init__.py'
      adding 'apex/parallel/distributed.py'
      adding 'apex/parallel/multiproc.py'
      adding 'apex/parallel/optimized_sync_batchnorm.py'
      adding 'apex/parallel/optimized_sync_batchnorm_kernel.py'
      adding 'apex/parallel/sync_batchnorm.py'
      adding 'apex/parallel/sync_batchnorm_kernel.py'
      adding 'apex/pyprof/__init__.py'
      adding 'apex/pyprof/nvtx/__init__.py'
      adding 'apex/pyprof/nvtx/nvmarker.py'
      adding 'apex/pyprof/parse/__init__.py'
      adding 'apex/pyprof/parse/__main__.py'
      adding 'apex/pyprof/parse/db.py'
      adding 'apex/pyprof/parse/kernel.py'
      adding 'apex/pyprof/parse/nvvp.py'
      adding 'apex/pyprof/parse/parse.py'
      adding 'apex/pyprof/prof/__init__.py'
      adding 'apex/pyprof/prof/__main__.py'
      adding 'apex/pyprof/prof/activation.py'
      adding 'apex/pyprof/prof/base.py'
      adding 'apex/pyprof/prof/blas.py'
      adding 'apex/pyprof/prof/conv.py'
      adding 'apex/pyprof/prof/convert.py'
      adding 'apex/pyprof/prof/data.py'
      adding 'apex/pyprof/prof/dropout.py'
      adding 'apex/pyprof/prof/embedding.py'
      adding 'apex/pyprof/prof/index_slice_join_mutate.py'
      adding 'apex/pyprof/prof/linear.py'
      adding 'apex/pyprof/prof/loss.py'
      adding 'apex/pyprof/prof/misc.py'
      adding 'apex/pyprof/prof/normalization.py'
      adding 'apex/pyprof/prof/optim.py'
      adding 'apex/pyprof/prof/output.py'
      adding 'apex/pyprof/prof/pointwise.py'
      adding 'apex/pyprof/prof/pooling.py'
      adding 'apex/pyprof/prof/prof.py'
      adding 'apex/pyprof/prof/randomSample.py'
      adding 'apex/pyprof/prof/recurrentCell.py'
      adding 'apex/pyprof/prof/reduction.py'
      adding 'apex/pyprof/prof/softmax.py'
      adding 'apex/pyprof/prof/usage.py'
      adding 'apex/pyprof/prof/utility.py'
      adding 'apex/reparameterization/__init__.py'
      adding 'apex/reparameterization/reparameterization.py'
      adding 'apex/reparameterization/weight_norm.py'
      adding 'apex-0.1.dist-info/LICENSE'
      adding 'apex-0.1.dist-info/METADATA'
      adding 'apex-0.1.dist-info/WHEEL'
      adding 'apex-0.1.dist-info/top_level.txt'
      adding 'apex-0.1.dist-info/RECORD'
      removing build/bdist.linux-x86_64/wheel
    [?25hdone
      Created wheel for apex: filename=apex-0.1-cp36-none-any.whl size=192848 sha256=959eeb55c66861e31142a303f69144ec4605c708e76b35d74c98498910b8b2ee
      Stored in directory: /tmp/pip-ephem-wheel-cache-u1piuhr8/wheels/b1/3a/aa/d84906eaab780ae580c7a5686a33bf2820d8590ac3b60d5967
      Removing source in /tmp/pip-req-build-4ehxv_ht
    Successfully built apex
    Installing collected packages: apex
    
    Successfully installed apex-0.1
    Cleaning up...
    Removed build tracker '/tmp/pip-req-tracker-5o9btbxy'
    




```python
from google.colab import auth
auth.authenticate_user()
from googleapiclient.discovery import build
import io
from googleapiclient.http import MediaIoBaseDownload
import matplotlib.pyplot as plt

drive_service = build('drive', 'v3')

def download_file(file_id, filepath):
    request = drive_service.files().get_media(fileId=file_id)
    downloaded = io.BytesIO()
    downloader = MediaIoBaseDownload(downloaded, request)
    done = False
    while done is False:
        # _ is a placeholder for a progress object that we ignore.
        # (Our file is small, so we skip reporting progress.)
        _, done = downloader.next_chunk()

    downloaded.seek(0)
    with open(filepath, "wb") as fp:
        fp.write(downloaded.read())
    #rint('Downloaded file contents are: {}'.format(downloaded.read()))
download_file("101g6XHACr0cwgXBf8LgFfNrHR3OPLBHv", "models/large/checkpoints/step_40000000.ckpt")

```


```python
! mkdir deep_privacy/detection/dsfd/weights
download_file("1WeXlNYsM6dMP3xQQELI-4gxhwKUQxc3-", "deep_privacy/detection/dsfd/weights/WIDERFace_DSFD_RES152.pth")

```


```python
! ls 
```

    adc.json  deep_privacy	images	sample_data
    apex	  DeepPrivacy	models	setup.sh
    


```python
from deep_privacy.config_parser import load_config
from deep_privacy.inference import infer, deep_privacy_anonymizer
import torch
```

    Imageio: 'ffmpeg-linux64-v3.3.1' was not found on your computer; downloading it now.
    Try 1. Download from https://github.com/imageio/imageio-binaries/raw/master/ffmpeg/ffmpeg-linux64-v3.3.1 (43.8 MB)
    Downloading: 8192/45929032 bytes (0.0%)1097728/45929032 bytes (2.4%)3227648/45929032 bytes (7.0%)6144000/45929032 bytes (13.4%)9437184/45929032 bytes (20.5%)13180928/45929032 bytes (28.7%)16678912/45929032 bytes (36.3%)19890176/45929032 bytes (43.3%)23388160/45929032 bytes (50.9%)26886144/45929032 bytes (58.5%)30359552/45929032 bytes (66.1%)33832960/45929032 bytes (73.7%)37339136/45929032 bytes (81.3%)41058304/45929032 bytes (89.4%)44597248/45929032 bytes (97.1%)45929032/45929032 bytes (100.0%)
      Done
    File saved as /root/.imageio/ffmpeg/ffmpeg-linux64-v3.3.1.
    

    Downloading: "https://download.pytorch.org/models/keypointrcnn_resnet50_fpn_coco-fc266e95.pth" to /root/.cache/torch/hub/checkpoints/keypointrcnn_resnet50_fpn_coco-fc266e95.pth
    


    HBox(children=(FloatProgress(value=0.0, max=237034793.0), HTML(value='')))


    
    


```python
config = load_config("models/large/config.yml")
checkpoint = torch.load("models/large/checkpoints/step_40000000.ckpt")
generator = infer.init_generator(config, checkpoint)
```

    extending G 512
    extending G 512
    extending G 512
    extending G 256
    extending G 128
    


```python
anonymizer = deep_privacy_anonymizer.DeepPrivacyAnonymizer(generator,
                                                           batch_size=32,
                                                           use_static_z=True,
                                                           keypoint_threshold=.1,
                                                           face_threshold=.6)
```

    Anonymizer initialized. Keypoint threshold: 0.1Face threshold: 0.6
    

# Anonymize images



```python
# Download images
! mkdir images
! wget https://www1.pictures.stylebistro.com/gi/Lupita+Nyong+o+Short+Hairstyles+Side+Parted+ZG8osyjW8YQl.jpg -O images/example.jpg
plt.imshow(plt.imread("images/example.jpg"))
```

    mkdir: cannot create directory ‘images’: File exists
    --2020-08-19 09:25:57--  https://www1.pictures.stylebistro.com/gi/Lupita+Nyong+o+Short+Hairstyles+Side+Parted+ZG8osyjW8YQl.jpg
    Resolving www1.pictures.stylebistro.com (www1.pictures.stylebistro.com)... 151.101.1.129, 151.101.65.129, 151.101.129.129, ...
    Connecting to www1.pictures.stylebistro.com (www1.pictures.stylebistro.com)|151.101.1.129|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 66379 (65K) [image/jpeg]
    Saving to: ‘images/example.jpg’
    
    images/example.jpg  100%[===================>]  64.82K  --.-KB/s    in 0.03s   
    
    2020-08-19 09:25:57 (2.15 MB/s) - ‘images/example.jpg’ saved [66379/66379]
    
    




    <matplotlib.image.AxesImage at 0x7fcaeb1379b0>




    
![png](output_13_2.png)
    



```python
anonymizer.anonymize_image_paths(["images/example.jpg"], ["images/example_anonymized.jpg"])
```

    Batch detecting faces:   0%|          | 0/1 [00:00<?, ?it/s]

    Finished loading DSFD model!
    

    Batch detecting faces: 100%|██████████| 1/1 [00:03<00:00,  3.18s/it]
    Keypoint inference: 100%|██████████| 1/1 [00:00<00:00,  2.33it/s]
    Anonyimizing faces: 100%|██████████| 1/1 [00:00<00:00,  8.13it/s]
    Post-processing: 100%|██████████| 1/1 [00:00<00:00, 36.22it/s]
    


```python
plt.figure(figsize=(8,16))
plt.imshow(plt.imread("images/example_anonymized.jpg"))
```




    <matplotlib.image.AxesImage at 0x7fcae8a72198>




    
![png](output_15_1.png)
    



```python
plt.figure(figsize=(16,40))
plt.imshow(plt.imread("images/example_anonymized_detected_left_anonymized_right.jpg"))
```




    <matplotlib.image.AxesImage at 0x7fcae6ede908>




    
![png](output_16_1.png)
    



```python

```
