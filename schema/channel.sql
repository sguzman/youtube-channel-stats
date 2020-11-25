create table channels
(
	id bigserial not null,
	serial char(25) not null
);

create unique index channels_id_uindex
	on channels (id);

create unique index channels_serial_uindex
	on channels (serial);

alter table channels
	add constraint channels_pk
		primary key (id);

