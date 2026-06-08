class ImageService:

    def generate_image(
        self,
        job_id,
        prompt
    ):

        file_path = f"/tmp/{job_id}.txt"

        with open(
            file_path,
            "w"
        ) as file:

            file.write(
                f"Generated content for: {prompt}"
            )

        return file_path


image_service = ImageService()