idf_component_register(SRCS "sketch.ino.cpp" "CommandHandler.cpp"
                    INCLUDE_DIRS "."
		    REQUIRES arduino nina-fw mbedtls driver wpa_supplicant)
