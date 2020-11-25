create table youtube.public.channels
(
	id bigserial not null,
	serial char(25) not null
);

create unique index channels_id_uindex
	on youtube.public.channels (id);

create unique index channels_serial_uindex
	on youtube.public.channels (serial);

alter table youtube.public.channels
	add constraint channels_pk
		primary key (id);

