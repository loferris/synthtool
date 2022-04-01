# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: metadata.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="metadata.proto",
    package="yoshi.synth.metadata",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x0emetadata.proto\x12\x14yoshi.synth.metadata\x1a\x1fgoogle/protobuf/timestamp.proto"\xf6\x01\n\x08Metadata\x12\x33\n\x0bupdate_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x02\x18\x01\x12-\n\x07sources\x18\x02 \x03(\x0b\x32\x1c.yoshi.synth.metadata.Source\x12\x37\n\x0c\x64\x65stinations\x18\x03 \x03(\x0b\x32!.yoshi.synth.metadata.Destination\x12\x34\n\tnew_files\x18\x04 \x03(\x0b\x32\x1d.yoshi.synth.metadata.NewFileB\x02\x18\x01\x12\x17\n\x0fgenerated_files\x18\x05 \x03(\t"\xb8\x01\n\x06Source\x12.\n\x03git\x18\x01 \x01(\x0b\x32\x1f.yoshi.synth.metadata.GitSourceH\x00\x12:\n\tgenerator\x18\x02 \x01(\x0b\x32%.yoshi.synth.metadata.GeneratorSourceH\x00\x12\x38\n\x08template\x18\x03 \x01(\x0b\x32$.yoshi.synth.metadata.TemplateSourceH\x00\x42\x08\n\x06source"m\n\tGitSource\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06remote\x18\x02 \x01(\t\x12\x0b\n\x03sha\x18\x03 \x01(\t\x12\x14\n\x0cinternal_ref\x18\x04 \x01(\t\x12\x12\n\nlocal_path\x18\x05 \x01(\t\x12\x0b\n\x03log\x18\x06 \x01(\t"F\n\x0fGeneratorSource\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x14\n\x0c\x64ocker_image\x18\x03 \x01(\t"?\n\x0eTemplateSource\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06origin\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t"\x94\x01\n\x0b\x44\x65stination\x12\x39\n\x06\x63lient\x18\x01 \x01(\x0b\x32\'.yoshi.synth.metadata.ClientDestinationH\x00\x12;\n\x07\x66ileset\x18\x02 \x01(\x0b\x32(.yoshi.synth.metadata.FileSetDestinationH\x00\x42\r\n\x0b\x44\x65stination"\x17\n\x07NewFile\x12\x0c\n\x04path\x18\x01 \x01(\t"\x7f\n\x11\x43lientDestination\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x10\n\x08\x61pi_name\x18\x02 \x01(\t\x12\x13\n\x0b\x61pi_version\x18\x03 \x01(\t\x12\x10\n\x08language\x18\x04 \x01(\t\x12\x11\n\tgenerator\x18\x05 \x01(\t\x12\x0e\n\x06\x63onfig\x18\x06 \x01(\t"3\n\x12\x46ileSetDestination\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\r\n\x05\x66iles\x18\x02 \x03(\tb\x06proto3',
    dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,],
)


_METADATA = _descriptor.Descriptor(
    name="Metadata",
    full_name="yoshi.synth.metadata.Metadata",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="update_time",
            full_name="yoshi.synth.metadata.Metadata.update_time",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\030\001",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="sources",
            full_name="yoshi.synth.metadata.Metadata.sources",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="destinations",
            full_name="yoshi.synth.metadata.Metadata.destinations",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="new_files",
            full_name="yoshi.synth.metadata.Metadata.new_files",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\030\001",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="generated_files",
            full_name="yoshi.synth.metadata.Metadata.generated_files",
            index=4,
            number=5,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=74,
    serialized_end=320,
)


_SOURCE = _descriptor.Descriptor(
    name="Source",
    full_name="yoshi.synth.metadata.Source",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="git",
            full_name="yoshi.synth.metadata.Source.git",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="generator",
            full_name="yoshi.synth.metadata.Source.generator",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="template",
            full_name="yoshi.synth.metadata.Source.template",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="source",
            full_name="yoshi.synth.metadata.Source.source",
            index=0,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
    ],
    serialized_start=323,
    serialized_end=507,
)


_GITSOURCE = _descriptor.Descriptor(
    name="GitSource",
    full_name="yoshi.synth.metadata.GitSource",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="yoshi.synth.metadata.GitSource.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="remote",
            full_name="yoshi.synth.metadata.GitSource.remote",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="sha",
            full_name="yoshi.synth.metadata.GitSource.sha",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="internal_ref",
            full_name="yoshi.synth.metadata.GitSource.internal_ref",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="local_path",
            full_name="yoshi.synth.metadata.GitSource.local_path",
            index=4,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="log",
            full_name="yoshi.synth.metadata.GitSource.log",
            index=5,
            number=6,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=509,
    serialized_end=618,
)


_GENERATORSOURCE = _descriptor.Descriptor(
    name="GeneratorSource",
    full_name="yoshi.synth.metadata.GeneratorSource",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="yoshi.synth.metadata.GeneratorSource.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="version",
            full_name="yoshi.synth.metadata.GeneratorSource.version",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="docker_image",
            full_name="yoshi.synth.metadata.GeneratorSource.docker_image",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=620,
    serialized_end=690,
)


_TEMPLATESOURCE = _descriptor.Descriptor(
    name="TemplateSource",
    full_name="yoshi.synth.metadata.TemplateSource",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="yoshi.synth.metadata.TemplateSource.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="origin",
            full_name="yoshi.synth.metadata.TemplateSource.origin",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="version",
            full_name="yoshi.synth.metadata.TemplateSource.version",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=692,
    serialized_end=755,
)


_DESTINATION = _descriptor.Descriptor(
    name="Destination",
    full_name="yoshi.synth.metadata.Destination",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="client",
            full_name="yoshi.synth.metadata.Destination.client",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="fileset",
            full_name="yoshi.synth.metadata.Destination.fileset",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="Destination",
            full_name="yoshi.synth.metadata.Destination.Destination",
            index=0,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
    ],
    serialized_start=758,
    serialized_end=906,
)


_NEWFILE = _descriptor.Descriptor(
    name="NewFile",
    full_name="yoshi.synth.metadata.NewFile",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="path",
            full_name="yoshi.synth.metadata.NewFile.path",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=908,
    serialized_end=931,
)


_CLIENTDESTINATION = _descriptor.Descriptor(
    name="ClientDestination",
    full_name="yoshi.synth.metadata.ClientDestination",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="source",
            full_name="yoshi.synth.metadata.ClientDestination.source",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="api_name",
            full_name="yoshi.synth.metadata.ClientDestination.api_name",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="api_version",
            full_name="yoshi.synth.metadata.ClientDestination.api_version",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="language",
            full_name="yoshi.synth.metadata.ClientDestination.language",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="generator",
            full_name="yoshi.synth.metadata.ClientDestination.generator",
            index=4,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="config",
            full_name="yoshi.synth.metadata.ClientDestination.config",
            index=5,
            number=6,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=933,
    serialized_end=1060,
)


_FILESETDESTINATION = _descriptor.Descriptor(
    name="FileSetDestination",
    full_name="yoshi.synth.metadata.FileSetDestination",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="source",
            full_name="yoshi.synth.metadata.FileSetDestination.source",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="files",
            full_name="yoshi.synth.metadata.FileSetDestination.files",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1062,
    serialized_end=1113,
)

_METADATA.fields_by_name[
    "update_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_METADATA.fields_by_name["sources"].message_type = _SOURCE
_METADATA.fields_by_name["destinations"].message_type = _DESTINATION
_METADATA.fields_by_name["new_files"].message_type = _NEWFILE
_SOURCE.fields_by_name["git"].message_type = _GITSOURCE
_SOURCE.fields_by_name["generator"].message_type = _GENERATORSOURCE
_SOURCE.fields_by_name["template"].message_type = _TEMPLATESOURCE
_SOURCE.oneofs_by_name["source"].fields.append(_SOURCE.fields_by_name["git"])
_SOURCE.fields_by_name["git"].containing_oneof = _SOURCE.oneofs_by_name["source"]
_SOURCE.oneofs_by_name["source"].fields.append(_SOURCE.fields_by_name["generator"])
_SOURCE.fields_by_name["generator"].containing_oneof = _SOURCE.oneofs_by_name["source"]
_SOURCE.oneofs_by_name["source"].fields.append(_SOURCE.fields_by_name["template"])
_SOURCE.fields_by_name["template"].containing_oneof = _SOURCE.oneofs_by_name["source"]
_DESTINATION.fields_by_name["client"].message_type = _CLIENTDESTINATION
_DESTINATION.fields_by_name["fileset"].message_type = _FILESETDESTINATION
_DESTINATION.oneofs_by_name["Destination"].fields.append(
    _DESTINATION.fields_by_name["client"]
)
_DESTINATION.fields_by_name["client"].containing_oneof = _DESTINATION.oneofs_by_name[
    "Destination"
]
_DESTINATION.oneofs_by_name["Destination"].fields.append(
    _DESTINATION.fields_by_name["fileset"]
)
_DESTINATION.fields_by_name["fileset"].containing_oneof = _DESTINATION.oneofs_by_name[
    "Destination"
]
DESCRIPTOR.message_types_by_name["Metadata"] = _METADATA
DESCRIPTOR.message_types_by_name["Source"] = _SOURCE
DESCRIPTOR.message_types_by_name["GitSource"] = _GITSOURCE
DESCRIPTOR.message_types_by_name["GeneratorSource"] = _GENERATORSOURCE
DESCRIPTOR.message_types_by_name["TemplateSource"] = _TEMPLATESOURCE
DESCRIPTOR.message_types_by_name["Destination"] = _DESTINATION
DESCRIPTOR.message_types_by_name["NewFile"] = _NEWFILE
DESCRIPTOR.message_types_by_name["ClientDestination"] = _CLIENTDESTINATION
DESCRIPTOR.message_types_by_name["FileSetDestination"] = _FILESETDESTINATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Metadata = _reflection.GeneratedProtocolMessageType(
    "Metadata",
    (_message.Message,),
    {
        "DESCRIPTOR": _METADATA,
        "__module__": "metadata_pb2"
        # @@protoc_insertion_point(class_scope:yoshi.synth.metadata.Metadata)
    },
)
_sym_db.RegisterMessage(Metadata)

Source = _reflection.GeneratedProtocolMessageType(
    "Source",
    (_message.Message,),
    {
        "DESCRIPTOR": _SOURCE,
        "__module__": "metadata_pb2"
        # @@protoc_insertion_point(class_scope:yoshi.synth.metadata.Source)
    },
)
_sym_db.RegisterMessage(Source)

GitSource = _reflection.GeneratedProtocolMessageType(
    "GitSource",
    (_message.Message,),
    {
        "DESCRIPTOR": _GITSOURCE,
        "__module__": "metadata_pb2"
        # @@protoc_insertion_point(class_scope:yoshi.synth.metadata.GitSource)
    },
)
_sym_db.RegisterMessage(GitSource)

GeneratorSource = _reflection.GeneratedProtocolMessageType(
    "GeneratorSource",
    (_message.Message,),
    {
        "DESCRIPTOR": _GENERATORSOURCE,
        "__module__": "metadata_pb2"
        # @@protoc_insertion_point(class_scope:yoshi.synth.metadata.GeneratorSource)
    },
)
_sym_db.RegisterMessage(GeneratorSource)

TemplateSource = _reflection.GeneratedProtocolMessageType(
    "TemplateSource",
    (_message.Message,),
    {
        "DESCRIPTOR": _TEMPLATESOURCE,
        "__module__": "metadata_pb2"
        # @@protoc_insertion_point(class_scope:yoshi.synth.metadata.TemplateSource)
    },
)
_sym_db.RegisterMessage(TemplateSource)

Destination = _reflection.GeneratedProtocolMessageType(
    "Destination",
    (_message.Message,),
    {
        "DESCRIPTOR": _DESTINATION,
        "__module__": "metadata_pb2"
        # @@protoc_insertion_point(class_scope:yoshi.synth.metadata.Destination)
    },
)
_sym_db.RegisterMessage(Destination)

NewFile = _reflection.GeneratedProtocolMessageType(
    "NewFile",
    (_message.Message,),
    {
        "DESCRIPTOR": _NEWFILE,
        "__module__": "metadata_pb2"
        # @@protoc_insertion_point(class_scope:yoshi.synth.metadata.NewFile)
    },
)
_sym_db.RegisterMessage(NewFile)

ClientDestination = _reflection.GeneratedProtocolMessageType(
    "ClientDestination",
    (_message.Message,),
    {
        "DESCRIPTOR": _CLIENTDESTINATION,
        "__module__": "metadata_pb2"
        # @@protoc_insertion_point(class_scope:yoshi.synth.metadata.ClientDestination)
    },
)
_sym_db.RegisterMessage(ClientDestination)

FileSetDestination = _reflection.GeneratedProtocolMessageType(
    "FileSetDestination",
    (_message.Message,),
    {
        "DESCRIPTOR": _FILESETDESTINATION,
        "__module__": "metadata_pb2"
        # @@protoc_insertion_point(class_scope:yoshi.synth.metadata.FileSetDestination)
    },
)
_sym_db.RegisterMessage(FileSetDestination)


_METADATA.fields_by_name["update_time"]._options = None
_METADATA.fields_by_name["new_files"]._options = None
# @@protoc_insertion_point(module_scope)