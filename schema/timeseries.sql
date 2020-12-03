create table stats
(
	time TIMESTAMPTZ default CURRENT_TIMESTAMP not null,
	id bigserial not null
		constraint stats_channels_id_fk
			references youtube.public.channels,
	subs int,
	vids int,
	views int
);

create unique index stats_time_uindex
	on stats (time);