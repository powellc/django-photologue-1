# -*- coding: utf-8 -*-
try:
    import Image
except ImportError:
    # Required PIL classes may or may not be available from the root namespace
    # depending on the installation method used.
    try:
        from PIL import Image
    except ImportError:
        raise ImportError('Photologue was unable to import the Python Imaging\
         Library. Please confirm it`s installed and available on your current\
          Python path.')

from photologue.models import PhotoEffect
from photologue.tests.helpers import PhotologueBaseTest

class PhotoEffectTest(PhotologueBaseTest):
    def test(self):
        effect = PhotoEffect(name='test')
        im = Image.open(self.pl.image.path)
        self.assert_(isinstance(effect.pre_process(im), Image.Image))
        self.assert_(isinstance(effect.post_process(im), Image.Image))
        self.assert_(isinstance(effect.process(im), Image.Image))

