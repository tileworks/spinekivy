from os.path import join
from kivy.core.image import ImageLoader

from spine.atlas.atlas import AtlasFormat
from spine.atlas.texture import TextureFilter, TextureWrap, \
    AbstractTextureLoader


class TextureLoader(AbstractTextureLoader):

    atlas_format_type = {
        AtlasFormat.Alpha: 'alpha',
        AtlasFormat.LuminanceAlpha: 'luminance_alpha',
        AtlasFormat.RGB888: 'rgb',
        AtlasFormat.RGBA8888: 'rgba'
    }

    texture_filter_type = {
        TextureFilter.Nearest: 'nearest',
        TextureFilter.Linear: 'linear',
        TextureFilter.MipMapNearestNearest: 'nearest_mipmap_nearest',
        TextureFilter.MipMapLinearNearest: 'linear_mipmap_nearest',
        TextureFilter.MipMapNearestLinear: 'nearest_mipmap_linear',
        TextureFilter.MipMapLinearLinear: 'linear_mipmap_linear'
    }

    texture_wrap_type = {
        TextureWrap.ClampToEdge: 'clamp_to_edge',
        TextureWrap.MirroredRepeat: 'mirrored_repeat',
        TextureWrap.Repeat: 'repeat'
    }

    def load(self, atlas_page, image_name):
        image = ImageLoader.load(join(self.images_path, image_name))
        texture = image.texture
        texture.mag_filter = self.texture_filter_type[atlas_page.mag_filter]
        texture.min_filter = self.texture_filter_type[atlas_page.min_filter]
        atlas_page.renderer_object = texture
        atlas_page.width = texture.width
        atlas_page.height = texture.height

    def unload(self, renderer_object):
        pass
