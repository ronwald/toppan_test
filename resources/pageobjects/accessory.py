class objects:
    nav_arrow_back = 'css:.navigation .arrow.back'
    nav_arrow_forward = 'css:.navigation .arrow.forward'
    nav_user = 'css:.user.pic'
    #nav_customize = 'xpath://div[@class="navs-wrapper"]/div[text()="CUSTOMIZE"]'
    #nav_performance = 'xpath://div[@class="navs-wrapper"]/div[text()=="PERFORMANCE"]'
    nav_lighting = 'xpath://div[@class="navs-wrapper"]/div[text()="LIGHTING"]'
    #nav_power = 'xpath://div[@class="navs-wrapper"]/div[text()=="POWER"]'
    #nav_calibration = 'xpath://div[@class="navs-wrapper"]/div[text()=="CALIBRATION"]'

    lighting_brightness_switch = 'css:.widget-col.col-left.flex .titleRow .title .switch'
    lighting_brightness_switch_on = 'css:.widget-col.col-left.flex .titleRow .title .switch.on'
    lighting_brightness_slider = 'css:.widget:nth-child(1) .slider-container > input'
    lighting_brightness_slider_on = 'css:.widget-col .slider-container.on'
    lighting_so_display_checkbox = 'css:.widget-col.col-left.flex .widget.has-slider .check-item:nth-child(2)'
    lighting_so_idle_checkbox = 'css:.widget-col.col-left.flex .widget.has-slider  .check-item'
    lighting_modes_quick_tab = 'css:.modes-tab:nth-child(1)'
    lighting_modes_advanced_tab = 'css:.modes-tab:nth-child(2)'
    lighting_color_dropdown = 'css:.has-color > .dropdown-area.dropdown-color'
    lighting_color_dropdown_2 = 'css:.has-color ~ .has-color > .dropdown-area.dropdown-color'
    lighting_color_preset = 'css:.presets > .preset[style="background: rgb({});"]'
    lighting_custom_preset_edit = 'xpath://div[@class="right-click show"]/div[text()="edit"]'
    lighting_random_color_preset = 'css:.presets > .preset:nth-child({})'
    lighting_custom_preset = 'css:.presets.custom > .preset:nth-child(2)'
    lighting_custom_hex_fld = 'css:.color-control > input.hex'
    lighting_custom_save_btn = 'css:.thx-btn:nth-child(2)'
    lighting_effect_dropdown = 'css:.chroma-flex-row .s3-dropdown'
    lighting_effect_option = 'xpath://div[@class="s3-options unsetZ flex expand"]/div[text()="{}"]'
    lighting_options_dropdown = 'css:.flex.chroma-flex-row > .dropdown-area > .s3-dropdown'
    lighting_advanced_effects_tab = 'css:.col-right .modes-tabs.dual.flex > *:nth-child(2)'
    lighting_quick_effects_tab = 'css:.col-right .modes-tabs.dual.flex > *:nth-child(1)'
    lighting_effectmode_active = 'css:.widget .modes-tab.lighting-effect.active'
    lighting_quick_effects_selected = 'css:.col-right .s3-dropdown .selected'
    lighting_preset_no_color = 'css:.presets > .no-color'

    # Lighting Tooltip text
    lighting_brightness_help_icon = 'css:.col-right .widget:nth-child(1) .slider-container + div .help'
    lighting_brightness_help_tip = lighting_brightness_help_icon + ' + div'
    lighting_brightness_help_tip_text = 'Adjust the brightness of your device’s lighting.'
    lighting_swlight_help_icon = 'css:.col-left .widget.has-slider .help'
    lighting_swlight_help_tip = 'css:.col-left .widget.has-slider .tip'
    lighting_swlight_help_tip_text = 'Customize when the device’s lighting will turn off.'
    lighting_effects_help_icon = 'css:.col-right > [style="flex: initial;"] .help'
    lighting_effects_help_tip = lighting_effects_help_icon + ' + .tip'
    lighting_effects_help_tip_text = 'Customize your device’s lighting effect from a list of presets, and synchronize it with other Razer Chroma devices that support the selected lighting effect'

    # breathing
    breathing_color_1_dropdown = 'css:.effects-area > .has-color:nth-child(1) .s3-dropdown'
    breathing_color_2_dropdown = 'css:.effects-area > .has-color:nth-child(2) .s3-dropdown'
    breathing_random_checkbox = 'css:[for="randColor"]'
    
    #audio meter
    am_color_boost_fld = 'css:.effects-area > div > .stepper > input'

    # reactive level
    lighting_reactive_level_slider = 'css:#reactiveSlider .slider-container > input'

    # Mouse Dock Chroma
    toolbar_title = 'xpath://div[@class="toolbar flex "]/div[2]'

    # Mouse Dock switch off lighting (sol)
    sol_check_display = 'css:[for="checkDisplay"]'
    sol_checkbox_display = 'css:#checkDisplay'
    sol_checkbox = 'css:.col-left> .widget:nth-child(2) .check-item'
    sol_display_checkbox_off = sol_checkbox + '.disabled'
    
    # Mouse dock chroma - brgihtness widget
    widget_title = 'xpath://div[text()="BRIGHTNESS" and @class="title"]'
    lighting_brightness_slider_off= 'xpath://div[@class="slider-container    "]/input[@class="slider"]'
