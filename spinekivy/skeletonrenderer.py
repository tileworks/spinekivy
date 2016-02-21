from os.path import basename, dirname
from spine.animation.animationstate import AnimationState
from spine.animation.animationstatedata import AnimationStateData
from spine.atlas.atlas import Atlas
from spine.attachment.attachment import AttachmentType
from spine.skeleton.skeleton import Skeleton
from spine.skeleton.skeletonjson import SkeletonJson

from spinekivy.atlasattachmentloader import AtlasAttachmentLoader
from spinekivy.textureloader import TextureLoader

_REGION_INDICES = range(4)


class SkeletonRenderer(object):

    def __init__(self):
        self.skeleton = None
        self.state = None
        self.scale = 1.0
        self.sprites = []

    def load(self, path):
        skeleton_data = self._load_skeleton_data(path)
        self.skeleton = Skeleton(skeleton_data)
        self.state = AnimationState(AnimationStateData(skeleton_data))

    def _load_skeleton_data(self, path):
        with open(path + '.json') as fp:
            json_text = fp.read()
        atlas = self._load_atlas(path)
        attachment_loader = AtlasAttachmentLoader(atlas)
        skeleton_json = SkeletonJson(attachment_loader)
        skeleton_json.scale = self.scale
        return skeleton_json.read_data(json_text, basename(path))

    def _load_atlas(self, path):
        with open(path + '.atlas') as fp:
            atlas_text = fp.read()
        texture_loader = TextureLoader(dirname(path))
        return Atlas(atlas_text, texture_loader)

    def update(self, dt):
        state = self.state
        skeleton = self.skeleton
        sprites = self.sprites
        state.update(dt)
        state.apply(skeleton)
        skeleton.update_world_transform()
        i = -1
        for slot in skeleton.draw_order:
            i += 1
            attachment = slot.attachment
            sprite = sprites[i]
            if not attachment:
                sprite.color.a = 0.0
            elif attachment.type == AttachmentType.region:
                mesh = sprite.mesh
                attachment.compute_world_vertices_uvs(slot, mesh.vertices)
                mesh.indices[:] = _REGION_INDICES
                mesh.mode = 'triangle_fan'
                mesh.texture = attachment.renderer_object
                sprite.color.rgba[:] = (slot.r, slot.g, slot.b, slot.a)
            elif attachment.type == AttachmentType.mesh:
                mesh = sprite.mesh
                attachment.compute_world_vertices_uvs(slot, mesh.vertices)
                mesh.mode = 'triangles'
                mesh.indices[:] = attachment.triangles
                mesh.texture = attachment.renderer_object
                sprite.color.rgba[:] = (slot.r, slot.g, slot.b, slot.a)
            elif attachment.type == AttachmentType.skinnedmesh:
                mesh = sprite.mesh
                attachment.compute_world_vertices_uvs(slot, mesh.vertices)
                mesh.mode = 'triangles'
                mesh.indices[:] = attachment.triangles
                mesh.texture = attachment.renderer_object
                sprite.color.rgba[:] = (slot.r, slot.g, slot.b, slot.a)
            elif attachment.type == AttachmentType.boundingbox:
                sprite.color.a = 0.0
            else:
                raise TypeError(
                    'Unknown attachment: {}'.format(type(attachment))
                )
