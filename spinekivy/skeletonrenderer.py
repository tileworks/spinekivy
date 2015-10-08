from os.path import join as join_path

from spine.animation.animationstate import AnimationState
from spine.animation.animationstatedata import AnimationStateData
from spine.atlas.atlas import Atlas
from spine.attachment.atlasattachmentloader import AtlasAttachmentLoader
from spine.attachment.attachment import AttachmentType
from spine.skeleton.skeleton import Skeleton
from spine.skeleton.skeletonjson import SkeletonJson

from textureloader import TextureLoader


class SkeletonRenderer(object):

    def __init__(self):
        self.skeleton = None
        self.state = None
        self.scale = 1.0
        self.sprites = []

    def load(self, path, name):
        skeleton_data = self._load_skeleton_data(path, name)
        self.skeleton = Skeleton(skeleton_data)
        self.state = AnimationState(AnimationStateData(skeleton_data))

    def _load_atlas(self, path, name):
        with open(join_path(path, name + '.atlas')) as fp:
            atlas_text = fp.read()
        texture_loader = TextureLoader(path)
        return Atlas(atlas_text, texture_loader)
    
    def _load_skeleton_data(self, path, name):
        with open(join_path(path, name + '.json')) as fp:
            json_text = fp.read()
        atlas = self._load_atlas(path, name)
        attachment_loader = AtlasAttachmentLoader(atlas)
        skeleton_json = SkeletonJson(attachment_loader)
        skeleton_json.scale = self.scale
        return skeleton_json.read_data(json_text, name)

    def update(self, dt):
        state = self.state
        skeleton = self.skeleton
        state.update(dt)
        state.apply(skeleton)
        skeleton.update_world_transform()

    def draw(self):
        skeleton = self.skeleton
        sprites = self.sprites
        for i, slot in enumerate(skeleton.draw_order):
            attachment = slot.attachment
            sprite = sprites[i]
            if attachment is None:
                sprite.color.a = 0.0
            elif attachment.type == AttachmentType.region:
                sprite_mesh = sprite.mesh
                attachment.compute_vertices_with_uvs(skeleton.x,
                                                     skeleton.y,
                                                     slot.bone,
                                                     sprite_mesh.vertices)
                indices = sprite_mesh.indices
                if len(indices) == 4:
                    indices[0] = 0
                    indices[1] = 1
                    indices[2] = 2
                    indices[3] = 3
                else:
                    indices[:] = range(4)
                sprite_mesh.mode = 'triangle_fan'
                sprite_mesh.texture = attachment.\
                    renderer_object.page.renderer_object
                sprite.color.rgba = (slot.r, slot.g, slot.b, slot.a)

            elif attachment.type == AttachmentType.mesh:
                sprite_mesh = sprite.mesh
                attachment.\
                    compute_world_vertices_with_uvs(skeleton.x,
                                                    skeleton.y,
                                                    slot,
                                                    sprite_mesh.vertices)
                sprite_mesh.mode = 'triangles'
                sprite_mesh.indices = attachment.triangles
                sprite_mesh.texture = attachment.\
                    renderer_object.page.renderer_object
                sprite.color.rgba = (slot.r, slot.g, slot.b, slot.a)

            elif attachment.type == AttachmentType.skinnedmesh:
                sprite_mesh = sprite.mesh
                attachment.\
                    compute_world_vertices_with_uvs(skeleton.x,
                                                    skeleton.y,
                                                    slot,
                                                    sprite_mesh.vertices)
                sprite_mesh.mode = 'triangles'
                sprite_mesh.indices = attachment.triangles
                sprite_mesh.texture = attachment.\
                    renderer_object.page.renderer_object
                sprite.color.rgba = (slot.r, slot.g, slot.b, slot.a)
