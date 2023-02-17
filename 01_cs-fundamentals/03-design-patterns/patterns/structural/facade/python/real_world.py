from pattern import VideoConverter

class VideoProcessingService:
    """A real-world service that uses the VideoConverter facade to handle user uploads."""
    
    def __init__(self):
        self.converter = VideoConverter()
        
    def process_user_video(self, user_name: str, filename: str):
        print(f"\nProcessing video for user: {user_name}")
        
        # User doesn't need to know how FFmpeg works, they just want an mp4
        output_file = self.converter.convert(filename, "mp4")
        
        print(f"File {output_file} is now ready for streaming on the platform.")

if __name__ == "__main__":
    service = VideoProcessingService()
    service.process_user_video("Alice", "vlog_001.raw")
    service.process_user_video("Bob", "holiday.mkv")
