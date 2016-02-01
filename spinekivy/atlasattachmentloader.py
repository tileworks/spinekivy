from spine.attachment.atlasattachmentloader import \
    AtlasAttachmentLoader as _AtlasAttachmentLoader


class AtlasAttachmentLoader(_AtlasAttachmentLoader):

    def new_region_attachment(self, skin, name, path):
        attachment = super(AtlasAttachmentLoader, self)\
            .new_region_attachment(skin, name, path)
        texture = attachment.renderer_object.page.renderer_object
        attachment.renderer_object = texture
        return attachment

    def new_mesh_attachment(self, skin, name, path):
        attachment = super(AtlasAttachmentLoader, self)\
            .new_mesh_attachment(skin, name, path)
        texture = attachment.renderer_object.page.renderer_object
        attachment.renderer_object = texture
        return attachment

    def new_skinned_mesh_attachment(self, skin, name, path):
        attachment = super(AtlasAttachmentLoader, self)\
            .new_skinned_mesh_attachment(skin, name, path)
        texture = attachment.renderer_object.page.renderer_object
        attachment.renderer_object = texture
        return attachment
