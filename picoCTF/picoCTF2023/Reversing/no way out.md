> Put this flag in standard picoCTF format before submitting. If the flag was h1_1m_7h3_f14g submit picoCTF{h1_1m_7h3_f14g} to the platform.

```
// EvolveGames.PlayerController
// Token: 0x06000021 RID: 33 RVA: 0x00002E70 File Offset: 0x00001070
private void Update()
{
	if (!this.characterController.isGrounded && !this.isClimbing)
	{
		this.moveDirection.y = this.moveDirection.y - this.gravity * Time.deltaTime;
	}
	Vector3 a = base.transform.TransformDirection(Vector3.forward);
	Vector3 a2 = base.transform.TransformDirection(Vector3.right);
	this.isRunning = (!this.isCrough && this.CanRunning && Input.GetKey(KeyCode.LeftShift));
	this.vertical = (this.canMove ? ((this.isRunning ? this.RunningValue : this.WalkingValue) * Input.GetAxis("Vertical")) : 0f);
	this.horizontal = (this.canMove ? ((this.isRunning ? this.RunningValue : this.WalkingValue) * Input.GetAxis("Horizontal")) : 0f);
	if (this.isRunning)
	{
		this.RunningValue = Mathf.Lerp(this.RunningValue, this.RuningSpeed, this.timeToRunning * Time.deltaTime);
	}
	else
	{
		this.RunningValue = this.WalkingValue;
	}
	float y = this.moveDirection.y;
	this.moveDirection = a * this.vertical + a2 * this.horizontal;
	if (Input.GetButton("Jump") && this.canMove && this.characterController.isGrounded && !this.isClimbing)
	{
		this.moveDirection.y = this.jumpSpeed;
	}
	else
	{
		this.moveDirection.y = y;
	}
	this.characterController.Move(this.moveDirection * Time.deltaTime);
	this.Moving = (this.horizontal < 0f || this.vertical < 0f || this.horizontal > 0f || this.vertical > 0f);
	if (Cursor.lockState == CursorLockMode.Locked && this.canMove)
	{
		this.Lookvertical = -Input.GetAxis("Mouse Y");
		this.Lookhorizontal = Input.GetAxis("Mouse X");
		this.rotationX += this.Lookvertical * this.lookSpeed;
		this.rotationX = Mathf.Clamp(this.rotationX, -this.lookXLimit, this.lookXLimit);
		this.Camera.transform.localRotation = Quaternion.Euler(this.rotationX, 0f, 0f);
		base.transform.rotation *= Quaternion.Euler(0f, this.Lookhorizontal * this.lookSpeed, 0f);
		if (this.isRunning && this.Moving)
		{
			this.cam.fieldOfView = Mathf.Lerp(this.cam.fieldOfView, this.RunningFOV, this.SpeedToFOV * Time.deltaTime);
		}
		else
		{
			this.cam.fieldOfView = Mathf.Lerp(this.cam.fieldOfView, this.InstallFOV, this.SpeedToFOV * Time.deltaTime);
		}
	}
	RaycastHit raycastHit;
	if (Input.GetKey(this.CroughKey))
	{
		this.isCrough = true;
		float height = Mathf.Lerp(this.characterController.height, this.CroughHeight, 5f * Time.deltaTime);
		this.characterController.height = height;
		this.WalkingValue = Mathf.Lerp(this.WalkingValue, this.CroughSpeed, 6f * Time.deltaTime);
	}
	else if (!Physics.Raycast(base.GetComponentInChildren<Camera>().transform.position, base.transform.TransformDirection(Vector3.up), out raycastHit, 0.8f, 1) && this.characterController.height != this.InstallCroughHeight)
	{
		this.isCrough = false;
		float height2 = Mathf.Lerp(this.characterController.height, this.InstallCroughHeight, 6f * Time.deltaTime);
		this.characterController.height = height2;
		this.WalkingValue = Mathf.Lerp(this.WalkingValue, this.walkingSpeed, 4f * Time.deltaTime);
	}
	RaycastHit raycastHit2;
	if (this.WallDistance != Physics.Raycast(base.GetComponentInChildren<Camera>().transform.position, base.transform.TransformDirection(Vector3.forward), out raycastHit2, this.HideDistance, this.LayerMaskInt) && this.CanHideDistanceWall)
	{
		this.WallDistance = Physics.Raycast(base.GetComponentInChildren<Camera>().transform.position, base.transform.TransformDirection(Vector3.forward), out raycastHit2, this.HideDistance, this.LayerMaskInt);
		this.Items.ani.SetBool("Hide", this.WallDistance);
		this.Items.DefiniteHide = this.WallDistance;
	}
}
```

코드를 보면 dnspy를 통해 해당 폴더 내 Assembly-CSharp.dll 파일을 열고 Evolvegames → PlayerController → Update()를 확인해보면 다음과 같다

```
// EvolveGames.PlayerController
// Token: 0x06000021 RID: 33 RVA: 0x00002E70 File Offset: 0x00001070
private void Update()
{
	if (!this.characterController.isGrounded && !this.isClimbing)
	{
		this.moveDirection.y = this.moveDirection.y - this.gravity * Time.deltaTime;
	}
	Vector3 a = base.transform.TransformDirection(Vector3.forward);
	Vector3 a2 = base.transform.TransformDirection(Vector3.right);
	this.isRunning = (!this.isCrough && this.CanRunning && Input.GetKey(KeyCode.LeftShift));
	this.vertical = (this.canMove ? ((this.isRunning ? this.RunningValue : this.WalkingValue) * Input.GetAxis("Vertical")) : 0f);
	this.horizontal = (this.canMove ? ((this.isRunning ? this.RunningValue : this.WalkingValue) * Input.GetAxis("Horizontal")) : 0f);
	if (this.isRunning)
	{
		this.RunningValue = Mathf.Lerp(this.RunningValue, this.RuningSpeed, this.timeToRunning * Time.deltaTime);
	}
	else
	{
		this.RunningValue = this.WalkingValue;
	}
	float y = this.moveDirection.y;
	this.moveDirection = a * this.vertical + a2 * this.horizontal;
	if (Input.GetButton("Jump") && this.canMove && this.characterController.isGrounded && !this.isClimbing)
	{
		this.moveDirection.y = this.jumpSpeed;
	}
	else
	{
		this.moveDirection.y = y;
	}
	this.characterController.Move(this.moveDirection * Time.deltaTime);
	this.Moving = (this.horizontal < 0f || this.vertical < 0f || this.horizontal > 0f || this.vertical > 0f);
	if (Cursor.lockState == CursorLockMode.Locked && this.canMove)
	{
		this.Lookvertical = -Input.GetAxis("Mouse Y");
		this.Lookhorizontal = Input.GetAxis("Mouse X");
		this.rotationX += this.Lookvertical * this.lookSpeed;
		this.rotationX = Mathf.Clamp(this.rotationX, -this.lookXLimit, this.lookXLimit);
		this.Camera.transform.localRotation = Quaternion.Euler(this.rotationX, 0f, 0f);
		base.transform.rotation *= Quaternion.Euler(0f, this.Lookhorizontal * this.lookSpeed, 0f);
		if (this.isRunning && this.Moving)
		{
			this.cam.fieldOfView = Mathf.Lerp(this.cam.fieldOfView, this.RunningFOV, this.SpeedToFOV * Time.deltaTime);
		}
		else
		{
			this.cam.fieldOfView = Mathf.Lerp(this.cam.fieldOfView, this.InstallFOV, this.SpeedToFOV * Time.deltaTime);
		}
	}
	RaycastHit raycastHit;
	if (Input.GetKey(this.CroughKey))
	{
		this.isCrough = true;
		float height = Mathf.Lerp(this.characterController.height, this.CroughHeight, 5f * Time.deltaTime);
		this.characterController.height = height;
		this.WalkingValue = Mathf.Lerp(this.WalkingValue, this.CroughSpeed, 6f * Time.deltaTime);
	}
	else if (!Physics.Raycast(base.GetComponentInChildren<Camera>().transform.position, base.transform.TransformDirection(Vector3.up), out raycastHit, 0.8f, 1) && this.characterController.height != this.InstallCroughHeight)
	{
		this.isCrough = false;
		float height2 = Mathf.Lerp(this.characterController.height, this.InstallCroughHeight, 6f * Time.deltaTime);
		this.characterController.height = height2;
		this.WalkingValue = Mathf.Lerp(this.WalkingValue, this.walkingSpeed, 4f * Time.deltaTime);
	}
	RaycastHit raycastHit2;
	if (this.WallDistance != Physics.Raycast(base.GetComponentInChildren<Camera>().transform.position, base.transform.TransformDirection(Vector3.forward), out raycastHit2, this.HideDistance, this.LayerMaskInt) && this.CanHideDistanceWall)
	{
		this.WallDistance = Physics.Raycast(base.GetComponentInChildren<Camera>().transform.position, base.transform.TransformDirection(Vector3.forward), out raycastHit2, this.HideDistance, this.LayerMaskInt);
		this.Items.ani.SetBool("Hide", this.WallDistance);
		this.Items.DefiniteHide = this.WallDistance;
	}
}
```

게임을 해보면 사다리를 올라가면 뭔가 넘고 싶은 곳이 생기는데 막힌다. 이를 해결하기 위해 점프를 할 때 떨어지는걸 막아보도록 한다

```
if (Input.GetButton("Jump") && this.canMove && this.characterController.isGrounded && !this.isClimbing)
{
    this.moveDirection.y = this.jumpSpeed;
}
```

코드에 있는 if문이 점프하는 동작인것 같아서 isGrounded를 지운다

`flag: picoCTF{welcome_to_unity!!}`
